# Generated by Django 2.2.13 on 2021-07-11 18:10

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogSettings', '0004_auto_20210711_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site_intro_context',
            name='subscribe_newslater_description',
            field=tinymce.models.HTMLField(default='Subscribe to our RSS feeds and newslater for quick updates', max_length=255),
        ),
    ]