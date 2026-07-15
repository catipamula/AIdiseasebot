import os
from django.core.asgi import get_asgi_application
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chatbot.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'symptom_checker.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chatbot.routing.websocket_urlpatterns
        )
    ),
})

# Serve development static assets when the application is launched directly
# through Daphne. Production deployments should serve static files separately.
application = ASGIStaticFilesHandler(application)
