# Generated by Django 2.1.5 on 2019-06-20 16:13

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0075_auto_20190607_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='_extra_fields',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experimentaldesign',
            name='_extra_fields_datasets',
            field=django_mysql.models.ListTextField(models.CharField(blank=True, max_length=100, null=True), blank=True, null=True, size=None, verbose_name='Extra Fields for Datasets'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='_individual',
            field=models.ManyToManyField(blank=True, to='Records.Individual', verbose_name='Individual Identifier'),
        ),
    ]
