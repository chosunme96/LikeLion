# Generated by Django 2.1.5 on 2019-02-21 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0005_applicant_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.Applicant')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.Application')),
            ],
        ),
    ]
