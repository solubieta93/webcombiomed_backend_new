# Generated by Django 3.0.5 on 2020-04-13 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_files'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='files',
            new_name='json_files',
        ),
    ]
