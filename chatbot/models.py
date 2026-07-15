from django.db import models

class ChatHistory(models.Model):
    user_input = models.TextField()
    ai_reply = models.TextField()
    embedding = models.JSONField()  # stores list of floats

    def __str__(self):
        return f"ChatHistory: {self.user_input[:50]}"
