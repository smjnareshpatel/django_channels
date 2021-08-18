import json
# chat/consumers.py

from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from django.core.serializers import serialize
from django.utils import timezone
from django.core.paginator import Paginator
import json
import asyncio
from django.core import serializers
from myapp.models import UserJsonData, LastAccessData
from channels.db import database_sync_to_async
from rest_framework.serializers import ModelSerializer

class UserJsonDataSer(ModelSerializer):
    class Meta:
        model = UserJsonData
        fields = "__all__"

class SockConsumer(AsyncWebsocketConsumer):
    ses = None 
    tot = 100
    async def connect(self):
            await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        pass

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        print(text_data,'fields')
        print('hello')
        print(self.scope['headers'][3][1].decode('utf-8'))
        self.ses = self.scope['headers'][3][1].decode('utf-8')
        items = None
        if text_data == 'NEXT':
            print('iniffffffffffffffff')
            tot = 100
            items = await self.get_or_create_sess(self.ses, self.tot)
            # print('item',len(items))
            await self.send(text_data=json.dumps({'status': 'hello bro', 'data': items}))

        else:
            await self.send(text_data=json.dumps({'message': 'what do you want?'}))





    @database_sync_to_async
    def get_or_create_sess(self, ses, tot):
        items = None
        obj, stat = LastAccessData.objects.get_or_create(session_id=self.ses)
        if stat:
            obj.last_access_id = self.tot
            obj.item_sent = self.tot
            # print('self.tot',self.tot)
            qs = UserJsonData.objects.all().order_by('id')[:100]
            print(qs.count())
            items = UserJsonDataSer(qs, many=True).data
            print('items',len(items))
        else:
            obj.last_access_id = self.tot + int(obj.last_access_id)
            obj.item_sent = self.tot
            print('hsoshgoa')
            # print('(tot +int(obj.last_access_id)',(tot +int(obj.last_access_id)))
            items = UserJsonDataSer(UserJsonData.objects.all().order_by('id')[int(obj.last_access_id):(tot +int(obj.last_access_id))], many=True).data

        obj.save()
        # print(items)
        return items