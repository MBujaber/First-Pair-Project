# Generated by Django 4.1.2 on 2022-10-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_booking_booked_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='book_seats',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
