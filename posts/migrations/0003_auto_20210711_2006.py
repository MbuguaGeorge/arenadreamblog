# Generated by Django 2.2.13 on 2021-07-11 17:06

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210711_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customizesettings',
            options={'verbose_name_plural': 'Blog settings'},
        ),
        migrations.AddField(
            model_name='customizesettings',
            name='overview_text',
            field=tinymce.models.HTMLField(default='Arena fitness gym is aimed towards building a fit community in all fields. Enjoy!!'),
        ),
        migrations.AddField(
            model_name='customizesettings',
            name='random_content',
            field=tinymce.models.HTMLField(default='Random page content will appear here'),
        ),
        migrations.AddField(
            model_name='customizesettings',
            name='site_intro_context',
            field=tinymce.models.HTMLField(default='Welcome arena fitness gym where fitness is not an option'),
        ),
        migrations.AddField(
            model_name='customizesettings',
            name='site_intro_heading',
            field=models.CharField(default='Quick intro to our site', max_length=100),
        ),
        migrations.AddField(
            model_name='customizesettings',
            name='subscribe_newslater_description',
            field=tinymce.models.HTMLField(default='Subscribe to our RSS feeds and newslater for quick updates'),
        ),
        migrations.AlterField(
            model_name='customizesettings',
            name='blogname',
            field=models.CharField(max_length=100),
        ),
    ]
