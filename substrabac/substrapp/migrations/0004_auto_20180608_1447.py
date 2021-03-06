# Generated by Django 2.0.5 on 2018-06-08 14:47

from django.db import migrations, models
import substrapp.models.algo
import substrapp.models.data
import substrapp.models.dataOpener
import substrapp.models.problem


class Migration(migrations.Migration):

    dependencies = [
        ('substrapp', '0003_algo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algo',
            name='algo',
            field=models.FileField(upload_to=substrapp.models.algo.upload_to),
        ),
        migrations.AlterField(
            model_name='data',
            name='features',
            field=models.FileField(upload_to=substrapp.models.data.upload_to),
        ),
        migrations.AlterField(
            model_name='data',
            name='labels',
            field=models.FileField(upload_to=substrapp.models.data.upload_to),
        ),
        migrations.AlterField(
            model_name='dataopener',
            name='script',
            field=models.FileField(upload_to=substrapp.models.dataOpener.upload_to),
        ),
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.FileField(upload_to=substrapp.models.problem.upload_to),
        ),
        migrations.AlterField(
            model_name='problem',
            name='metrics',
            field=models.FileField(upload_to=substrapp.models.problem.upload_to),
        ),
    ]
