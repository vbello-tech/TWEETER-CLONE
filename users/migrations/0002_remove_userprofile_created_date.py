# Generated by Django 4.0.6 on 2022-10-09 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='created_date',
        ),
    ]
