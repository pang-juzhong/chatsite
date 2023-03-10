import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

from . import routings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatsite.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    #AuthMiddleware认证，可以获取到用户信息
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(routings.websocket_urlpatterns),
        )
    ),
})
