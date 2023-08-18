import logging
import json
from channels.generic.websocket import AsyncWebsocketConsumer

from gateway_app.constants import CONSTANTS


logger = logging.getLogger(__name__)


class WebSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.group_name = CONSTANTS["gateway_group_name"]

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        logger.info('Websocket connection opened.')

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        logger.info('Websocket connection closed.')

    async def send_message(self, event):
        data = event['data']
        logger.info('Send the incoming http requests to the websocket. \nData:')
        logger.info(data)
        await self.send(json.dumps(data))
