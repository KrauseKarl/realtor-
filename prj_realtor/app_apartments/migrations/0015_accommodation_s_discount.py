# Generated by Django 4.0 on 2022-07-14 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_apartments', '0014_alter_accommodation_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodation',
            name='s_discount',
            field=models.BooleanField(default=False, verbose_name='спец.предложение'),
        ),
    ]
