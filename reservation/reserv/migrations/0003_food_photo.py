# Generated by Django 2.2.6 on 2019-11-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserv', '0002_food_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
