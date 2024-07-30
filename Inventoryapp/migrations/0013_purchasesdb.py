# Generated by Django 5.0.3 on 2024-04-07 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventoryapp', '0012_rename_sgtockquantity_purchase_stockquantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchasesdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppliername', models.CharField(blank=True, max_length=100, null=True)),
                ('suppliermobileno', models.IntegerField(blank=True, null=True)),
                ('suppliergstin', models.CharField(max_length=100, null=True)),
                ('stockprice', models.PositiveIntegerField(blank=True, null=True)),
                ('stockquantity', models.PositiveIntegerField(blank=True, null=True)),
                ('totalprice', models.IntegerField(blank=True, null=True)),
                ('stock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inventoryapp.stocksdb')),
            ],
        ),
    ]