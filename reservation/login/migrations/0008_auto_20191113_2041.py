# Generated by Django 2.2.6 on 2019-11-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_restaurant_current_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='current_customer',
            field=models.IntegerField(default=0),
        ),
    ]
