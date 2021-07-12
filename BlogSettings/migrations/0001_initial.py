# Generated by Django 3.2.5 on 2021-07-12 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogintroheading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_intro_heading', models.CharField(default='Quick intro to our site', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Set blog intro context heading',
            },
        ),
        migrations.CreateModel(
            name='Customblogname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogname', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Blog name',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/images/%d/')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Gallery',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Helpdesk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.TextField(default='Siriba campus - Nyawita', max_length=255)),
                ('physical_location', models.CharField(default='Maseno student center - Wing A', max_length=255)),
                ('email', models.EmailField(default='asiafric@gmail.com', max_length=100)),
                ('tel', models.CharField(default='254711349412', max_length=12)),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('youtube', models.URLField()),
                ('instagram', models.URLField()),
                ('other', models.URLField(default='enter any aditional social media url')),
                ('rights_year', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Help desk setup',
            },
        ),
        migrations.CreateModel(
            name='OverViewtext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overview_text', models.TextField(default='Arena fitness gym is aimed towards building a fit community in all fields.\n\n Enjoy!!', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'set blog overview text',
            },
        ),
        migrations.CreateModel(
            name='Ranks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Site_intro_context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_intro_context', models.TextField(default='Welcome arena fitness gym where fitness is not an option', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Set intro context',
            },
        ),
        migrations.CreateModel(
            name='Site_random_context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('random_content', models.TextField(default='Random page content will appear here', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Set random content',
            },
        ),
        migrations.CreateModel(
            name='Subscribe_newslater_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe_newslater_description', models.TextField(default='Subscribe to our RSS feeds and newslater for quick updates', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Subscribe Newslate description',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('dateadded', models.DateTimeField(auto_now_add=True, null=True)),
                ('rank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BlogSettings.ranks')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Set Contacts',
            },
        ),
    ]
