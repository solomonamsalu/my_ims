# Generated by Django 4.1.2 on 2022-12-10 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_item'),
        ('purchase', '0002_alter_purhaseorder_amount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PurhaseOrder',
            new_name='Purchaseorder',
        ),
    ]
