# Generated by Django 2.1.5 on 2019-02-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0056_auto_20190211_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailedfield',
            name='_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Name'),
        ),
    ]