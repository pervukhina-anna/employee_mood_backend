import json

from channels.generic.websocket import AsyncWebsocketConsumer


class UserNotifyConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.ws_id = self.scope['url_route']['kwargs']['id']
        self.group_name = 'ws_%s' % self.ws_id
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name, self.channel_name
        )
        await self.close()

    async def notification(self, event):
        data = event['data']
        await self.send(json.dumps(data, default=str))