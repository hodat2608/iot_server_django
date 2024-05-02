from django.db import models
from server.models import server_test

class x75(models.Model):
    
    client = models.ForeignKey(server_test,on_delete=models.CASCADE,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_on_excel = models.CharField(max_length=255,null=True, blank=True)
    lot = models.CharField(max_length=255,null=True, blank=True)
    status = models.BooleanField(default=False)

class category(models.Model):
    date = models.ForeignKey(x75,on_delete=models.CASCADE,null=True)
    ngay_san_xuat = models.CharField(max_length=255,null=True, blank=True)
    gio_luu_du_lieu = models.CharField(max_length=255,null=True, blank=True)
    tong_sl_sx = models.IntegerField(null=True, blank=True)
    tong_sl_pp_kx = models.IntegerField(null=True, blank=True)
    tay_choi = models.IntegerField(null=True, blank=True)
    chau_dien = models.IntegerField(null=True, blank=True)
    buichi_chau= models.IntegerField(null=True, blank=True)
    buichi_choi= models.IntegerField(null=True, blank=True)
    pp_khac = models.IntegerField(null=True, blank=True)
    ty_le_pdn =models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    luu_xuat = models.IntegerField(null=True, blank=True)
    luu_xuat_image = models.ImageField(upload_to='images/', null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']

class category_lddk(models.Model): 
    date_1 = models.ForeignKey(x75,on_delete=models.CASCADE,null=True)
    slsx = models.IntegerField(null=True, blank=True, default= 0)
    slpp= models.IntegerField(null=True, blank=True, default= 0)
    qc_choi= models.IntegerField(null=True, blank=True, default= 0)
    ng_choi= models.IntegerField(null=True, blank=True, default= 0)
    nham_choi= models.IntegerField(null=True, blank=True, default= 0)
    qc_chau= models.IntegerField(null=True, blank=True, default= 0)
    ng_chau= models.IntegerField(null=True, blank=True, default= 0)
    nham_chau= models.IntegerField(null=True, blank=True, default= 0)
    qc_bc_choi= models.IntegerField(null=True, blank=True, default= 0)
    ng_bc_choi= models.IntegerField(null=True, blank=True, default= 0)
    nham_bc_choi= models.IntegerField(null=True, blank=True, default= 0)
    qc_bc_chau= models.IntegerField(null=True, blank=True, default= 0)
    ng_bc_chau= models.IntegerField(null=True, blank=True, default= 0)
    nham_bc_chau= models.IntegerField(null=True, blank=True, default= 0)
    qc_pp_khac= models.IntegerField(null=True, blank=True, default= 0)
    ng_pp_khac= models.IntegerField(null=True, blank=True, default= 0)
    nham_pp_khac= models.IntegerField(null=True, blank=True, default= 0)
    tong_pp_qc= models.IntegerField(null=True, blank=True, default= 0)
    tong_pp_cong_doan= models.IntegerField(null=True, blank=True, default= 0)
    tong_pp_pdn= models.IntegerField(null=True, blank=True, default= 0)
    luu_xuat= models.IntegerField(null=True, blank=True, default= 0)
    luu_xuat_image = models.ImageField(upload_to='images/', null=True,blank=True)
    note = models.CharField(max_length=20,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


