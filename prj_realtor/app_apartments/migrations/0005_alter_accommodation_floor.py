# Generated by Django 4.0 on 2022-07-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_apartments', '0004_accommodation_apartment_complex_accommodation_floor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='floor',
            field=models.PositiveIntegerField(default=1, verbose_name='этаж'),
        ),
    ]