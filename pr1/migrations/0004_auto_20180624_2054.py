# Generated by Django 2.0.6 on 2018-06-24 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr1', '0003_auto_20180617_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zadanie',
            name='context',
            field=models.CharField(max_length=500),
        ),
    ]
