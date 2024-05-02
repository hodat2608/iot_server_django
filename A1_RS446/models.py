from django.db import models
from server.models import server_test

class A1(models.Model):
    client = models.ForeignKey(server_test,on_delete=models.CASCADE,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_on_excel = models.CharField(max_length=255,null=True, blank=True)
    lot = models.CharField(max_length=255,null=True, blank=True)
    status = models.BooleanField(default=False)

class category(models.Model):
    date = models.ForeignKey(A1,on_delete=models.CASCADE,null=True)
    ngay_san_xuat = models.CharField(max_length=255,null=True, blank=True)
    gio_luu_du_lieu = models.CharField(max_length=255,null=True, blank=True)
    tong_sl_sx = models.IntegerField(null=True, blank=True)
    tong_sl_pp_kx = models.IntegerField(null=True, blank=True)
    tay_choi = models.IntegerField(null=True, blank=True)
    chau_dien = models.IntegerField(null=True, blank=True)
    buichi= models.IntegerField(null=True, blank=True)
    divat= models.IntegerField(null=True, blank=True)
    cacbon= models.IntegerField(null=True, blank=True)
    me_de= models.IntegerField(null=True, blank=True)
    pp_khac = models.IntegerField(null=True, blank=True)
    ty_le_pdn =models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    luu_xuat = models.IntegerField(null=True, blank=True)
    luu_xuat_image = models.ImageField(upload_to='images/', null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
