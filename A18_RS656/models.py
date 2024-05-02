from django.db import models
from server.models import server_test
from datetime import datetime

class A18(models.Model):
    
    client = models.ForeignKey(server_test,on_delete=models.CASCADE,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_on_excel = models.CharField(max_length=255,null=True, blank=True)
    lot = models.CharField(max_length=255,null=True, blank=True)
    status = models.BooleanField(default=False)
    shift_start_time = models.TimeField(null=True, blank=True)
    shift_end_time = models.TimeField(null=True, blank=True)
    total_operate_time = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.client} - {self.date_on_excel} "
    
    def calculate_total_operate_time(self):
        if self.shift_start_time and self.shift_end_time:
            FMT = '%H:%M:%S'
            tdelta = datetime.strptime(self.shift_end_time, FMT) - datetime.strptime(self.shift_start_time, FMT)
            self.total_operate_time = tdelta
        super().save()  

class category(models.Model):
    date = models.ForeignKey(A18,on_delete=models.CASCADE,null=True)
    ngay_san_xuat = models.CharField(max_length=255,null=True, blank=True)
    gio_luu_du_lieu = models.CharField(max_length=255,null=True, blank=True)
    tong_so_luong_sx = models.IntegerField(null=True, blank=True) 
    cuon_cam = models.IntegerField(null=True, blank=True)
    cacbon_tay_choi = models.IntegerField(null=True, blank=True)
    han_choi= models.IntegerField(null=True, blank=True)
    han_chau= models.IntegerField(null=True, blank=True)
    de_vo_nho = models.IntegerField(null=True, blank=True)
    tu_dien = models.IntegerField(null=True, blank=True)
    cong_chau_dien= models.IntegerField(null=True, blank=True)
    bui_chi = models.IntegerField(null=True, blank=True)
    phe_pham_khac = models.IntegerField(null=True, blank=True)
    tong_so_luong_pp = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.ngay_san_xuat