import os
import json
import asyncio
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from channels.generic.websocket import AsyncWebsocketConsumer

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

        await self.send(text_data=json.dumps({
            "message": "Hello! 👋 I'm your Disease Checker Bot.\n\nTell me your symptoms and I'll help you out."
        }))

    async def receive(self, text_data):

        data = json.loads(text_data)
        user_input = data["message"]

        prompt = f"""
A user reports the following symptoms or disease:

{user_input}

Respond in the following format:

Description:
- Explain the disease in simple language.

Tablets:
- Mention common medicines and their purpose.
- Advise consulting a doctor before taking medicines.

Precautions:
- List important precautions.

Recommended Foods:
- List foods that support recovery.

Foods to Avoid:
- List foods that should be avoided.

Natural Home Remedies:
- List home remedies if applicable.
"""

        try:

            response = await asyncio.wait_for(
                asyncio.to_thread(
                    client.chat.completions.create,
                    model="Qwen/Qwen2.5-7B-Instruct",
                    messages=[
                        {
                            "role": "system",
                            "content": """You are a professional, friendly medical assistant.
Never claim to be a doctor.
Always provide safe and educational information."""
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    max_tokens=700,
                    temperature=0.3
                ),
                timeout=60
            )

            ai_reply = response.choices[0].message.content

            formatted_reply = ai_reply.replace("\n", "\n\n")

        except asyncio.TimeoutError:
            formatted_reply = (
                "⚠️ Request timed out.\n\n"
                "Please try again after a few seconds."
            )

        except Exception as e:
            print("HF ERROR:", repr(e))

            formatted_reply = (
                "⚠️ AI service temporarily unavailable.\n\n"
                f"Error: {str(e)}"
            )

        await self.send(text_data=json.dumps({
            "message": formatted_reply
        }))