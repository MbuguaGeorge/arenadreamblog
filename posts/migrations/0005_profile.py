# Generated by Django 3.2.5 on 2021-07-11 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_delete_customizesettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='uploads/users/user.jpg', upload_to='uploads/users/%Y%m%d/')),
                ('email', models.EmailField(max_length=100)),
                ('website', models.URLField(blank=True, max_length=255, null=True)),
                ('biography', models.TextField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]