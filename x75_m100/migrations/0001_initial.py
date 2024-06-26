# Generated by Django 4.2.1 on 2024-02-16 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tong_sl_sx', models.IntegerField(blank=True, null=True)),
                ('tong_sl_pp_kx', models.IntegerField(blank=True, null=True)),
                ('tay_choi', models.IntegerField(blank=True, null=True)),
                ('chau_dien', models.IntegerField(blank=True, null=True)),
                ('buichi_chau', models.IntegerField(blank=True, null=True)),
                ('buichi_choi', models.IntegerField(blank=True, null=True)),
                ('pp_khac', models.IntegerField(blank=True, null=True)),
                ('ty_le_pdn', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('luu_xuat', models.IntegerField(blank=True, null=True)),
                ('luu_xuat_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='x75',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('lot', models.CharField(blank=True, max_length=7, null=True)),
                ('status', models.BooleanField(default=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='server.server_test')),
            ],
        ),
    ]
