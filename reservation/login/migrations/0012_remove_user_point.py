# Generated by Django 2.2.4 on 2019-11-27 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_user_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='point',
        ),
    ]