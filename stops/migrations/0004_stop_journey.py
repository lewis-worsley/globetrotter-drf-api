# Generated by Django 3.2.20 on 2023-08-09 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journeys', '0001_initial'),
        ('stops', '0003_remove_stop_journey'),
    ]

    operations = [
        migrations.AddField(
            model_name='stop',
            name='journey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stops', to='journeys.journey'),
            preserve_default=False,
        ),
    ]