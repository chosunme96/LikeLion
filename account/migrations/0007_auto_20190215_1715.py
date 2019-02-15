# Generated by Django 2.1.5 on 2019-02-15 08:15

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_registerlink'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registerlink',
            options={'verbose_name': '가입 링크', 'verbose_name_plural': '가입 링크(들)'},
        ),
        migrations.AlterField(
            model_name='registerlink',
            name='register_until',
            field=models.DateTimeField(default=account.models.get_time_limit),
        ),
    ]
