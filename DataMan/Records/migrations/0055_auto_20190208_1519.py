# Generated by Django 2.1.5 on 2019-02-08 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0054_auto_20190208_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileread',
            name='_File',
            field=models.FileField(upload_to='files/'),
        ),
    ]