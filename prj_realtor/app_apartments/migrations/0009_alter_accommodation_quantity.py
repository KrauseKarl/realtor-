# Generated by Django 4.0 on 2022-07-14 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_apartments', '0008_alter_accommodation_type_acc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='quantity',
            field=models.CharField(choices=[('zro', 'студия'), ('one', '1-комнатная'), ('two', '2-комнатная'), ('thr', '3-комнатная'), ('lrg', '4-комнатная'), ('ext', '5-комнатная')], default='one', max_length=3, verbose_name='кол-во комнат'),
        ),
    ]
