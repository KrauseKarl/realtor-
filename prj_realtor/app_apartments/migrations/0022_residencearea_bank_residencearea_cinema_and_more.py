# Generated by Django 4.0 on 2022-07-26 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_apartments', '0021_residencearea_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='residencearea',
            name='bank',
            field=models.SmallIntegerField(default=0, verbose_name='банки'),
        ),
        migrations.AddField(
            model_name='residencearea',
            name='cinema',
            field=models.SmallIntegerField(default=0, verbose_name='кино, театры'),
        ),
        migrations.AddField(
            model_name='residencearea',
            name='fitness_club',
            field=models.SmallIntegerField(default=0, verbose_name='спортзал'),
        ),
        migrations.AddField(
            model_name='residencearea',
            name='kindergarten',
            field=models.SmallIntegerField(default=0, verbose_name='дет.сад'),
        ),
        migrations.AddField(
            model_name='residencearea',
            name='park',
            field=models.SmallIntegerField(default=0, verbose_name='парки,скверы'),
        ),
        migrations.AddField(
            model_name='residencearea',
            name='post',
            field=models.SmallIntegerField(default=0, verbose_name='почта'),
        ),
        migrations.AddField(
            model_name='residencearea',
            name='school',
            field=models.SmallIntegerField(default=0, verbose_name='школы'),
        ),
        migrations.AddField(
            model_name='residencearea',
            name='shop',
            field=models.SmallIntegerField(default=0, verbose_name='магазин'),
        ),
        migrations.AddField(
            model_name='residencearea',
            name='spy',
            field=models.SmallIntegerField(default=0, verbose_name='салоны красоты'),
        ),
        migrations.AddField(
            model_name='residencearea',
            name='swimming_pool',
            field=models.SmallIntegerField(default=0, verbose_name='бассейн'),
        ),
        migrations.AlterField(
            model_name='residencearea',
            name='title',
            field=models.CharField(choices=[('Central', 'ЖК Центральный'), ('River', 'ЖК Речник'), ('Park', 'ЖК Парковый')], default='C', max_length=12, verbose_name='жилой комплекс'),
        ),
    ]
