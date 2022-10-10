# Generated by Django 4.1.2 on 2022-10-10 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sku_number', models.CharField(max_length=200)),
                ('selling_price', models.FloatField()),
                ('cost_price', models.FloatField()),
                ('max_stock', models.IntegerField()),
                ('onhand_stock', models.IntegerField()),
                ('reorder_point', models.IntegerField()),
                ('preferred_supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='inventory.supplier')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.store')),
            ],
        ),
    ]
