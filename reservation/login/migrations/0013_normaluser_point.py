# Generated by Django 2.2.4 on 2019-11-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_remove_user_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='normaluser',
            name='point',
            field=models.IntegerField(default=0),
        ),
    ]