# Generated by Django 3.2.20 on 2023-08-09 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stops', '0004_stop_journey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stop',
            name='journey',
        ),
    ]
