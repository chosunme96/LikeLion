# Generated by Django 2.1.5 on 2019-02-21 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('recruitment', '0004_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]
