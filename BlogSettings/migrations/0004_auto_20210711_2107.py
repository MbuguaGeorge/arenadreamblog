# Generated by Django 2.2.13 on 2021-07-11 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogSettings', '0003_auto_20210711_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overviewtext',
            name='overview_text',
            field=models.TextField(default='Arena fitness gym is aimed towards building a fit community in all fields.\n\n Enjoy!!', max_length=255),
        ),
    ]
