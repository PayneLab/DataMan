# Generated by Django 2.1.5 on 2019-02-13 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0058_fileread_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='_experimentalDesign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Records.ExperimentalDesign', verbose_name='Experimental Design'),
        ),
    ]