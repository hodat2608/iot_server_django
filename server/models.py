from django.db import models

class server_test(models.Model):
    name_client = models.CharField(max_length=255, null=True, blank=True)
    line = models.CharField(max_length=255, null=True, blank=True) 
    port = models.IntegerField(null=True, blank=True)
    host = models.GenericIPAddressField(null=True, blank=True)
    status = models.BooleanField(default=False)
    folder_path = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.name_client