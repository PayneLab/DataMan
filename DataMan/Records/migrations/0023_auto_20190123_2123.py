# Generated by Django 2.1.5 on 2019-01-24 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0022_auto_20190123_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sample',
            options={'ordering': ['_sampleName']},
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='sampleName',
            new_name='_sampleName',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='storageCondition',
            new_name='_storageCondition',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='storageLocation',
            new_name='_storageLocation',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='treatmentProtocol',
            new_name='_treatmentProtocol',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='_sample',
        ),
        migrations.AddField(
            model_name='sample',
            name='_experiment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Records.Experiment'),
        ),
    ]