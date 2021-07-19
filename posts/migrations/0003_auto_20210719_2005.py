# Generated by Django 3.1.4 on 2021-07-19 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210716_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='posts.author'),
        ),
    ]
