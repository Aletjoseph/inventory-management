# Generated by Django 5.0.3 on 2024-04-03 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventoryapp', '0004_purchasesdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppilerdb',
            name='s_gstin',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
