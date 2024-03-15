# Generated by Django 4.1.13 on 2024-03-15 09:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_rename_facility_badmintoncourtbooking_court_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badmintoncourtbooking',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='badmintoncourtbooking',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='futsalcourtbooking',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='futsalcourtbooking',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='tenniscourtbooking',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='tenniscourtbooking',
            name='start_time',
        ),
        migrations.AddField(
            model_name='badmintoncourtbooking',
            name='day',
            field=models.DateField(default=django.utils.timezone.localtime),
        ),
        migrations.AddField(
            model_name='badmintoncourtbooking',
            name='time',
            field=models.CharField(
                choices=[
                    (1, '12 AM - 1 AM'),
                    (2, '1 AM - 2 AM'),
                    (3, '2 AM - 3 AM'),
                    (4, '3 AM - 4 AM'),
                    (5, '4 AM - 5 AM'),
                    (6, '5 AM - 6 AM'),
                    (7, '6 AM - 7 AM'),
                    (8, '7 AM - 8 AM'),
                    (9, '8 AM - 9 AM'),
                    (10, '9 AM - 10 AM'),
                    (11, '10 AM - 11 AM'),
                    (12, '11 AM - 12 PM'),
                    (13, '12 PM - 1 PM'),
                    (14, '1 PM - 2 PM'),
                    (15, '2 PM - 3 PM'),
                    (16, '3 PM - 4 PM'),
                    (17, '4 PM - 5 PM'),
                    (18, '5 PM - 6 PM'),
                    (19, '6 PM - 7 PM'),
                    (20, '7 PM - 8 PM'),
                    (21, '8 PM - 9 PM'),
                    (22, '9 PM - 10 PM'),
                    (23, '10 PM - 11 PM'),
                    (24, '11 PM - 12 AM'),
                ],
                default=(1, '12 AM - 1 AM'),
                max_length=64,
            ),
        ),
        migrations.AddField(
            model_name='badmintoncourtbooking',
            name='time_ordered',
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
        migrations.AddField(
            model_name='futsalcourtbooking',
            name='day',
            field=models.DateField(default=django.utils.timezone.localtime),
        ),
        migrations.AddField(
            model_name='futsalcourtbooking',
            name='time',
            field=models.CharField(
                choices=[
                    (1, '12 AM - 1 AM'),
                    (2, '1 AM - 2 AM'),
                    (3, '2 AM - 3 AM'),
                    (4, '3 AM - 4 AM'),
                    (5, '4 AM - 5 AM'),
                    (6, '5 AM - 6 AM'),
                    (7, '6 AM - 7 AM'),
                    (8, '7 AM - 8 AM'),
                    (9, '8 AM - 9 AM'),
                    (10, '9 AM - 10 AM'),
                    (11, '10 AM - 11 AM'),
                    (12, '11 AM - 12 PM'),
                    (13, '12 PM - 1 PM'),
                    (14, '1 PM - 2 PM'),
                    (15, '2 PM - 3 PM'),
                    (16, '3 PM - 4 PM'),
                    (17, '4 PM - 5 PM'),
                    (18, '5 PM - 6 PM'),
                    (19, '6 PM - 7 PM'),
                    (20, '7 PM - 8 PM'),
                    (21, '8 PM - 9 PM'),
                    (22, '9 PM - 10 PM'),
                    (23, '10 PM - 11 PM'),
                    (24, '11 PM - 12 AM'),
                ],
                default=(1, '12 AM - 1 AM'),
                max_length=64,
            ),
        ),
        migrations.AddField(
            model_name='futsalcourtbooking',
            name='time_ordered',
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
        migrations.AddField(
            model_name='tenniscourtbooking',
            name='day',
            field=models.DateField(default=django.utils.timezone.localtime),
        ),
        migrations.AddField(
            model_name='tenniscourtbooking',
            name='time',
            field=models.CharField(
                choices=[
                    (1, '12 AM - 1 AM'),
                    (2, '1 AM - 2 AM'),
                    (3, '2 AM - 3 AM'),
                    (4, '3 AM - 4 AM'),
                    (5, '4 AM - 5 AM'),
                    (6, '5 AM - 6 AM'),
                    (7, '6 AM - 7 AM'),
                    (8, '7 AM - 8 AM'),
                    (9, '8 AM - 9 AM'),
                    (10, '9 AM - 10 AM'),
                    (11, '10 AM - 11 AM'),
                    (12, '11 AM - 12 PM'),
                    (13, '12 PM - 1 PM'),
                    (14, '1 PM - 2 PM'),
                    (15, '2 PM - 3 PM'),
                    (16, '3 PM - 4 PM'),
                    (17, '4 PM - 5 PM'),
                    (18, '5 PM - 6 PM'),
                    (19, '6 PM - 7 PM'),
                    (20, '7 PM - 8 PM'),
                    (21, '8 PM - 9 PM'),
                    (22, '9 PM - 10 PM'),
                    (23, '10 PM - 11 PM'),
                    (24, '11 PM - 12 AM'),
                ],
                default=(1, '12 AM - 1 AM'),
                max_length=64,
            ),
        ),
        migrations.AddField(
            model_name='tenniscourtbooking',
            name='time_ordered',
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
    ]
