# Generated by Django 3.0.5 on 2020-04-21 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200413_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='priority',
            field=models.IntegerField(default=-1),
        ),
    ]
