# Generated by Django 3.1 on 2020-08-08 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200808_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='', max_length=70, verbose_name='Breve descripcion'),
        ),
    ]
