# Generated by Django 3.0.5 on 2020-10-24 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_post_context'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='json_details',
            new_name='json_details_es',
        ),
    ]
