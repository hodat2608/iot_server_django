# Generated by Django 4.2.1 on 2024-02-16 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x75_m100', '0003_x75_date_on_excel_alter_x75_lot_alter_x75_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='gio_luu_du_lieu',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='ngay_san_xuat',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
