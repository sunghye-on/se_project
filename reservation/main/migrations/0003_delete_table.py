# Generated by Django 2.2.4 on 2019-11-09 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_table_table_sum'),
    ]

    operations = [
        migrations.DeleteModel(
            name='table',
        ),
    ]