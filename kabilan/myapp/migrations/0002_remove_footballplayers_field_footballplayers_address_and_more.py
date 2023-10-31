# Generated by Django 4.2.5 on 2023-10-31 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footballplayers',
            name='field',
        ),
        migrations.AddField(
            model_name='footballplayers',
            name='address',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='footballplayers',
            name='city',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
