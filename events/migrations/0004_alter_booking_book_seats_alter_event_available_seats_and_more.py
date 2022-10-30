# Generated by Django 4.1.2 on 2022-10-30 14:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_booking_book_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='book_seats',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1, 'Minimum seats is 1 seat.')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='available_seats',
            field=models.PositiveIntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='total_seats',
            field=models.PositiveIntegerField(default=20),
        ),
    ]