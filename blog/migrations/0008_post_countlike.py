# Generated by Django 2.1.4 on 2020-01-20 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200103_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='countLike',
            field=models.IntegerField(default=0),
        ),
    ]