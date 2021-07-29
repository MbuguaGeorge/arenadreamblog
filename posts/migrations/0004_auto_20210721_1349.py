# Generated by Django 3.1.4 on 2021-07-21 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20210719_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to='posts.Author'),
        ),
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='author_profile/'),
        ),
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
