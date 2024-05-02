from channels.generic.websocket import WebsocketConsumer
from threading import Thread
from .models import category
import json
import time
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from server.models import server_test
from A18_RS656.models import category,A18
import asyncio
from django.core.serializers.json import DjangoJSONEncoder
import datetime
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from channels.db import database_sync_to_async

class ChartDataRealtimeConsumer_Async(AsyncWebsocketConsumer): 
    async def connect(self):
        self.date_id = self.scope['url_route']['kwargs']['date_id']
        await self.accept()
        await self.fetch_chart_data()

    async def disconnect(self, close_code):
        pass

    async def fetch_chart_data(self):
        while True:
            queryset = await sync_to_async(category.objects.filter)(date_id=self.date_id)
            last_entry = await sync_to_async(queryset.order_by('-id').first)()
            if last_entry:
                last_entry_data = {
                    'date_id': last_entry.date_id,
                    'ngay_san_xuat': last_entry.ngay_san_xuat[:10],
                    'gio_luu_du_lieu': last_entry.gio_luu_du_lieu,
                    'tong_so_luong_sx': last_entry.tong_so_luong_sx,
                    'cuon_cam': last_entry.cuon_cam,
                    'cacbon_tay_choi': last_entry.cacbon_tay_choi,
                    'han_choi': last_entry.han_choi,
                    'han_chau': last_entry.han_chau,
                    'de_vo_nho': last_entry.de_vo_nho,
                    'tu_dien': last_entry.tu_dien,
                    'cong_chau_dien': last_entry.cong_chau_dien,
                    'bui_chi': last_entry.bui_chi,
                    'phe_pham_khac': last_entry.phe_pham_khac,
                    'tong_so_luong_pp': last_entry.tong_so_luong_pp
                }
                await self.send(text_data=json.dumps(last_entry_data))
            await asyncio.sleep(10)

class DetailDataRealtimeConsumer(WebsocketConsumer):

    def connect(self):
        self.date_id = self.scope['url_route']['kwargs']['date_id']
        print(self.date_id)
        self.accept()
        self.thread = None
        if self.date_id:
            self.thread = Thread(target=self.receiving)
            self.thread.daemon = True
            self.thread.start()

    def disconnect(self, close_code):
        pass

    def receiving(self):
        while True:
            last_entry = category.objects.filter(date_id=self.date_id).order_by('-id').first()
            if last_entry:
                last_entry_data = {
                    'ngay_san_xuat': last_entry.ngay_san_xuat[:10],
                    'gio_luu_du_lieu': last_entry.gio_luu_du_lieu,
                    'tong_so_luong_sx': last_entry.tong_so_luong_sx,
                    'cuon_cam': last_entry.cuon_cam,
                    'cacbon_tay_choi': last_entry.cacbon_tay_choi,
                    'han_choi': last_entry.han_choi,
                    'han_chau': last_entry.han_chau,
                    'de_vo_nho': last_entry.de_vo_nho,
                    'tu_dien': last_entry.tu_dien,
                    'cong_chau_dien': last_entry.cong_chau_dien,
                    'bui_chi': last_entry.bui_chi,
                    'phe_pham_khac': last_entry.phe_pham_khac,
                    'tong_so_luong_pp': last_entry.tong_so_luong_pp
                }
            data = category.objects.filter(date_id=self.date_id)
            serialized_data = [{'date_id': entry.date_id,
                        'ngay_san_xuat': entry.ngay_san_xuat[:10],
                        'gio_luu_du_lieu': entry.gio_luu_du_lieu,
                        'tong_so_luong_sx': entry.tong_so_luong_sx,
                        'cuon_cam': entry.cuon_cam,
                        'cacbon_tay_choi': entry.cacbon_tay_choi,
                        'han_choi': entry.han_choi,
                        'han_chau': entry.han_chau,
                        'de_vo_nho': entry.de_vo_nho,
                        'tu_dien': entry.tu_dien,
                        'cong_chau_dien': entry.cong_chau_dien,
                        'bui_chi': entry.bui_chi,
                        'phe_pham_khac': entry.phe_pham_khac,
                        'tong_so_luong_pp': entry.tong_so_luong_pp} for entry in data]
            combined_data = {
                    "serialized_data": serialized_data,
                    "last_entry_data": last_entry_data
                }

            self.send(text_data=json.dumps(combined_data))
            time.sleep(10)

class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.time)):
            return obj.isoformat()
        return super().default(obj)
    
class Detail_Date_RealTime(WebsocketConsumer):
    def connect(self):
        self.id = self.scope['url_route']['kwargs']['client_id']
        print(self.id)
        self.accept()
        self.thread = None
        if self.id:
            self.thread = Thread(target=self.receiving)
            self.thread.daemon = True
            self.thread.start()

    def disconnect(self, close_code):
        pass

    def format_time(time_obj):
        return time_obj.strftime('%H:%M:%S')

    def receiving(self):
        while True:
            date = A18.objects.filter(client_id = self.id).order_by('-id')[:10]
            name_space_id = server_test.objects.get(id=self.id)
            name_space = name_space_id.name_client
            serialized_data = [{'client_id': entry.client_id,
                        'date_created': entry.date_created,
                        'date_on_excel': entry.date_on_excel,
                        'lot': entry.lot,
                        'status': entry.status,
                        'shift_start_time': entry.shift_start_time,
                        'shift_end_time': entry.shift_end_time,
                        'total_operate_time': entry.total_operate_time,
                        'detail_url': f'/detail/{name_space}_detail_data/{entry.id}/',
                        'id': entry.id,
                       } for entry in date]
            self.send(text_data=json.dumps(serialized_data, cls = CustomJSONEncoder))
            time.sleep(30)

class ChartDateRealtimeConsumer_Async(AsyncWebsocketConsumer): 
    async def connect(self):
        self.id = self.scope['url_route']['kwargs']['id']
        await self.accept()
        await self.chart_date()

    async def disconnect(self, close_code):
        pass

    async def chart_date(self):
        while True:
            queryset = await sync_to_async(A18.objects.filter)(client_id=self.id)
            date = await sync_to_async(list)(queryset.order_by('-id')[:10]) 
            dat_and_last_records = []
            for dat in date:
                last_category_record = await sync_to_async(dat.category_set.order_by('id').last)()
                if last_category_record:
                    last_record_data = {
                        'tong_so_luong_sx': last_category_record.tong_so_luong_sx,
                        'tong_so_luong_pp': last_category_record.tong_so_luong_pp,
                    }
                else:
                    last_record_data = None
                dat_and_last_records.append({'date_on_excel': dat.date_on_excel,'lot': dat.lot, 'last_record': last_record_data,})
            await self.send(text_data=json.dumps({'dat_and_last_records': dat_and_last_records}))
            await asyncio.sleep(30) 