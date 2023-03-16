from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from board.consumers import *

application = ProtocolTypeRouter({
    'websocket' : AllowedHostsOriginValidator(
        URLRouter([
            path('', BoardConsumer.as_asgi())
        ])
    )
})