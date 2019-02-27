# Generated by Django 2.1.5 on 2019-02-22 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0060_auto_20190219_1102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detailedfield',
            options={'ordering': ['_name']},
        ),
        migrations.AlterModelOptions(
            name='individual',
            options={'ordering': ['_individualIdentifier']},
        ),
        migrations.RemoveField(
            model_name='individual',
            name='_individualName',
        ),
        migrations.AddField(
            model_name='individual',
            name='_age',
            field=models.TextField(default=1, verbose_name='Age'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='individual',
            name='_extra_fields',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='individual',
            name='_gender',
            field=models.TextField(default='M', verbose_name='Gender'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='individual',
            name='_healthStatus',
            field=models.TextField(default='N/a', verbose_name='Health Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='individual',
            name='_individualIdentifier',
            field=models.TextField(default='OLD RECORD', verbose_name='Individual Identifier'),
            preserve_default=False,
        ),
    ]
