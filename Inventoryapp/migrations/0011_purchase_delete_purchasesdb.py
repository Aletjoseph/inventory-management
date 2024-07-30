# Generated by Django 5.0.3 on 2024-04-07 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventoryapp', '0010_remove_purchasesdb_stockname_purchasesdb_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sgtockquantity', models.IntegerField()),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventoryapp.stocksdb')),
            ],
        ),
        migrations.DeleteModel(
            name='Purchasesdb',
        ),
    ]
