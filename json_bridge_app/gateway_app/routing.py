from django.urls import re_path

from gateway_app import consumers

websocket_urlpatterns = [
    re_path(r'ws/api/ui/$', consumers.WebSocketConsumer.as_asgi()),
]