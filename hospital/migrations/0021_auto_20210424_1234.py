# Generated by Django 3.1.5 on 2021-04-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_auto_20210424_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='calldate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='calltime',
            field=models.TimeField(null=True),
        ),
    ]