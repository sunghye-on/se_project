# Generated by Django 2.2.6 on 2019-11-13 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_restaurant_max_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='current_customer',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
