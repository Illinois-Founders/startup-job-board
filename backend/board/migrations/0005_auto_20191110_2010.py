# Generated by Django 2.2.6 on 2019-11-10 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_customuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='userPassword',
        ),
        migrations.RemoveField(
            model_name='startup',
            name='orgPassword',
        ),
    ]
