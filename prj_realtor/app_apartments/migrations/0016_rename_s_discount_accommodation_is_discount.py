# Generated by Django 4.0 on 2022-07-14 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_apartments', '0015_accommodation_s_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accommodation',
            old_name='s_discount',
            new_name='is_discount',
        ),
    ]
