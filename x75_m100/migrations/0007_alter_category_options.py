# Generated by Django 4.2.1 on 2024-03-28 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('x75_m100', '0006_alter_category_lddk_luu_xuat_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created']},
        ),
    ]
