# Generated by Django 4.1.2 on 2022-10-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
