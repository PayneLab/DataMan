# Generated by Django 2.1.5 on 2019-05-06 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0069_instrumentsetting_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='_acquisitionEnd',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Acquisition Date'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='_acquisitionStart',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Upload Date'),
        ),
    ]
