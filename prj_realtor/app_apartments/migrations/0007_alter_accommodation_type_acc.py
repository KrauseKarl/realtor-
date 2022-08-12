# Generated by Django 4.0 on 2022-07-13 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_apartments', '0006_alter_accommodation_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='type_acc',
            field=models.CharField(choices=[('std', 'студия'), ('rms', 'стандартная'), ('hfl', 'высокие потолки'), ('dpx', 'двухуровневая')], default='std', max_length=3, verbose_name='тип помещения'),
        ),
    ]
