# Generated by Django 5.0.3 on 2024-03-14 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventoryapp', '0002_rename_supplier_address_suppilerdb_s_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocksdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockname', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
