# Generated by Django 4.1.13 on 2024-03-15 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_remove_badmintoncourtbooking_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badmintoncourtbooking',
            name='time',
            field=models.CharField(
                choices=[
                    ('12 AM - 1 AM', '12 AM - 1 AM'),
                    ('1 AM - 2 AM', '1 AM - 2 AM'),
                    ('2 AM - 3 AM', '2 AM - 3 AM'),
                    ('3 AM - 4 AM', '3 AM - 4 AM'),
                    ('4 AM - 5 AM', '4 AM - 5 AM'),
                    ('5 AM - 6 AM', '5 AM - 6 AM'),
                    ('6 AM - 7 AM', '6 AM - 7 AM'),
                    ('7 AM - 8 AM', '7 AM - 8 AM'),
                    ('8 AM - 9 AM', '8 AM - 9 AM'),
                    ('9 AM - 10 AM', '9 AM - 10 AM'),
                    ('10 AM - 11 AM', '10 AM - 11 AM'),
                    ('11 AM - 12 PM', '11 AM - 12 PM'),
                    ('12 PM - 1 PM', '12 PM - 1 PM'),
                    ('1 PM - 2 PM', '1 PM - 2 PM'),
                    ('2 PM - 3 PM', '2 PM - 3 PM'),
                    ('3 PM - 4 PM', '3 PM - 4 PM'),
                    ('4 PM - 5 PM', '4 PM - 5 PM'),
                    ('5 PM - 6 PM', '5 PM - 6 PM'),
                    ('6 PM - 7 PM', '6 PM - 7 PM'),
                    ('7 PM - 8 PM', '7 PM - 8 PM'),
                    ('8 PM - 9 PM', '8 PM - 9 PM'),
                    ('9 PM - 10 PM', '9 PM - 10 PM'),
                    ('10 PM - 11 PM', '10 PM - 11 PM'),
                    ('11 PM - 12 AM', '11 PM - 12 AM'),
                ],
                default=('12 AM - 1 AM', '12 AM - 1 AM'),
                max_length=64,
            ),
        ),
        migrations.AlterField(
            model_name='futsalcourtbooking',
            name='time',
            field=models.CharField(
                choices=[
                    ('12 AM - 1 AM', '12 AM - 1 AM'),
                    ('1 AM - 2 AM', '1 AM - 2 AM'),
                    ('2 AM - 3 AM', '2 AM - 3 AM'),
                    ('3 AM - 4 AM', '3 AM - 4 AM'),
                    ('4 AM - 5 AM', '4 AM - 5 AM'),
                    ('5 AM - 6 AM', '5 AM - 6 AM'),
                    ('6 AM - 7 AM', '6 AM - 7 AM'),
                    ('7 AM - 8 AM', '7 AM - 8 AM'),
                    ('8 AM - 9 AM', '8 AM - 9 AM'),
                    ('9 AM - 10 AM', '9 AM - 10 AM'),
                    ('10 AM - 11 AM', '10 AM - 11 AM'),
                    ('11 AM - 12 PM', '11 AM - 12 PM'),
                    ('12 PM - 1 PM', '12 PM - 1 PM'),
                    ('1 PM - 2 PM', '1 PM - 2 PM'),
                    ('2 PM - 3 PM', '2 PM - 3 PM'),
                    ('3 PM - 4 PM', '3 PM - 4 PM'),
                    ('4 PM - 5 PM', '4 PM - 5 PM'),
                    ('5 PM - 6 PM', '5 PM - 6 PM'),
                    ('6 PM - 7 PM', '6 PM - 7 PM'),
                    ('7 PM - 8 PM', '7 PM - 8 PM'),
                    ('8 PM - 9 PM', '8 PM - 9 PM'),
                    ('9 PM - 10 PM', '9 PM - 10 PM'),
                    ('10 PM - 11 PM', '10 PM - 11 PM'),
                    ('11 PM - 12 AM', '11 PM - 12 AM'),
                ],
                default=('12 AM - 1 AM', '12 AM - 1 AM'),
                max_length=64,
            ),
        ),
        migrations.AlterField(
            model_name='tenniscourtbooking',
            name='time',
            field=models.CharField(
                choices=[
                    ('12 AM - 1 AM', '12 AM - 1 AM'),
                    ('1 AM - 2 AM', '1 AM - 2 AM'),
                    ('2 AM - 3 AM', '2 AM - 3 AM'),
                    ('3 AM - 4 AM', '3 AM - 4 AM'),
                    ('4 AM - 5 AM', '4 AM - 5 AM'),
                    ('5 AM - 6 AM', '5 AM - 6 AM'),
                    ('6 AM - 7 AM', '6 AM - 7 AM'),
                    ('7 AM - 8 AM', '7 AM - 8 AM'),
                    ('8 AM - 9 AM', '8 AM - 9 AM'),
                    ('9 AM - 10 AM', '9 AM - 10 AM'),
                    ('10 AM - 11 AM', '10 AM - 11 AM'),
                    ('11 AM - 12 PM', '11 AM - 12 PM'),
                    ('12 PM - 1 PM', '12 PM - 1 PM'),
                    ('1 PM - 2 PM', '1 PM - 2 PM'),
                    ('2 PM - 3 PM', '2 PM - 3 PM'),
                    ('3 PM - 4 PM', '3 PM - 4 PM'),
                    ('4 PM - 5 PM', '4 PM - 5 PM'),
                    ('5 PM - 6 PM', '5 PM - 6 PM'),
                    ('6 PM - 7 PM', '6 PM - 7 PM'),
                    ('7 PM - 8 PM', '7 PM - 8 PM'),
                    ('8 PM - 9 PM', '8 PM - 9 PM'),
                    ('9 PM - 10 PM', '9 PM - 10 PM'),
                    ('10 PM - 11 PM', '10 PM - 11 PM'),
                    ('11 PM - 12 AM', '11 PM - 12 AM'),
                ],
                default=('12 AM - 1 AM', '12 AM - 1 AM'),
                max_length=64,
            ),
        ),
    ]
