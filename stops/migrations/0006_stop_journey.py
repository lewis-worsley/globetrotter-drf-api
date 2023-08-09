# Generated by Django 3.2.20 on 2023-08-09 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journeys', '0001_initial'),
        ('stops', '0005_remove_stop_journey'),
    ]

    operations = [
        migrations.AddField(
            model_name='stop',
            name='journey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='journeys.journey'),
            preserve_default=False,
        ),
    ]