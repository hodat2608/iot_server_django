from django.db import models
from server.models import server_test
from datetime import datetime

class TAM_SAT_A75_M100(models.Model):
    
    client = models.ForeignKey(server_test,on_delete=models.CASCADE,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_on_excel = models.CharField(max_length=255,null=True, blank=True)
    lot = models.CharField(max_length=255,null=True, blank=True)
    status = models.BooleanField(default=False)
    shift_start_time = models.TimeField(null=True, blank=True)
    shift_end_time = models.TimeField(null=True, blank=True)
    total_operate_time = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.client}-{self.date_on_excel}"
    
    def calculate_total_operate_time(self):
        if self.shift_start_time and self.shift_end_time:
            FMT = '%H:%M:%S'
            tdelta = datetime.strptime(self.shift_end_time, FMT) - datetime.strptime(self.shift_start_time, FMT)
            self.total_operate_time = tdelta
        super().save()  

class category(models.Model):
    date = models.ForeignKey(TAM_SAT_A75_M100,on_delete=models.CASCADE,null=True)
    ngay_san_xuat = models.CharField(max_length=255,null=True, blank=True)
    gio_luu_du_lieu = models.CharField(max_length=255,null=True, blank=True)

    tong_so_luong_sx = models.IntegerField(null=True, blank=True) 

    keo_dinh_truc_cam_1 = models.IntegerField(null=True, blank=True) 
    keo_dinh_ban_comi_cam_1 =  models.IntegerField(null=True, blank=True)
    keo_it_keo_khong_deu_cam_1 = models.IntegerField(null=True, blank=True)
    keo_bi_thung_lo_cam_1 = models.IntegerField(null=True, blank=True)
    phe_pham_khac_cam_1 = models.IntegerField(null=True, blank=True)
    tong_so_luong_pp_cam_1 = models.IntegerField(null=True, blank=True)

    keo_dinh_truc_cam_2 = models.IntegerField(null=True, blank=True) 
    keo_dinh_ban_comi_cam_2 =  models.IntegerField(null=True, blank=True)
    keo_it_keo_khong_deu_cam_2 = models.IntegerField(null=True, blank=True)
    keo_bi_thung_lo_cam_2 = models.IntegerField(null=True, blank=True)
    phe_pham_khac_cam_2 = models.IntegerField(null=True, blank=True)
    tong_so_luong_pp_cam_2 = models.IntegerField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.ngay_san_xuat
    


# class category_lddk(models.Model): 
#     date_lddk = models.ForeignKey(TAM_SAT_A75_M100,on_delete=models.CASCADE,null=True)
#     slsx = models.IntegerField(null=True, blank=True, default= 0)
#     slpp = models.IntegerField(null=True, blank=True, default= 0)
#     qc_choi= models.IntegerField(null=True, blank=True, default= 0)
#     ng_choi= models.IntegerField(null=True, blank=True, default= 0)
#     nham_choi= models.IntegerField(null=True, blank=True, default= 0)
#     qc_chau= models.IntegerField(null=True, blank=True, default= 0)
#     ng_chau= models.IntegerField(null=True, blank=True, default= 0)
#     nham_chau= models.IntegerField(null=True, blank=True, default= 0)
#     qc_bc_choi= models.IntegerField(null=True, blank=True, default= 0)
#     ng_bc_choi= models.IntegerField(null=True, blank=True, default= 0)
#     nham_bc_choi= models.IntegerField(null=True, blank=True, default= 0)
#     qc_bc_chau= models.IntegerField(null=True, blank=True, default= 0)
#     ng_bc_chau= models.IntegerField(null=True, blank=True, default= 0)
#     nham_bc_chau= models.IntegerField(null=True, blank=True, default= 0)
#     qc_pp_khac= models.IntegerField(null=True, blank=True, default= 0)
#     ng_pp_khac= models.IntegerField(null=True, blank=True, default= 0)
#     nham_pp_khac= models.IntegerField(null=True, blank=True, default= 0)
#     tong_pp_qc= models.IntegerField(null=True, blank=True, default= 0)
#     tong_pp_cong_doan= models.IntegerField(null=True, blank=True, default= 0)
#     tong_pp_pdn= models.IntegerField(null=True, blank=True, default= 0)
#     luu_xuat= models.IntegerField(null=True, blank=True, default= 0)
#     luu_xuat_image = models.ImageField(upload_to='images/', null=True,blank=True)
#     note = models.CharField(max_length=20,null=True, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
