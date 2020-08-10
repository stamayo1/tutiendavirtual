# Generated by Django 3.1 on 2020-08-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200808_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='costoProducto',
            field=models.FloatField(default=0.0, verbose_name='Precio de compra'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_vnt',
            field=models.FloatField(default=0.0, verbose_name='Precio venta'),
        ),
    ]
