# Generated by Django 3.0.7 on 2021-01-21 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
    ]
