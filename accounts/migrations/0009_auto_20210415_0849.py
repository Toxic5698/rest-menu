# Generated by Django 3.1.7 on 2021-04-15 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210309_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='order',
            name='meal1',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Hlavní jídlo 1'),
        ),
        migrations.AlterField(
            model_name='order',
            name='meal2',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Hlavní jídlo 2'),
        ),
        migrations.AlterField(
            model_name='order',
            name='meal3',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Hlavní jídlo 3'),
        ),
        migrations.AlterField(
            model_name='order',
            name='meal4',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Hlavní jídlo 4'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Jméno'),
        ),
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.TextField(blank=True, default=None, max_length=999, null=True, verbose_name='Poznámka'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.PositiveIntegerField(null=True, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pickup',
            field=models.BooleanField(blank=True, default=False, verbose_name='S sebou'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pickup_time',
            field=models.CharField(blank=True, choices=[('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30')], default=False, max_length=200, verbose_name='Čas vyzvednutí'),
        ),
        migrations.AlterField(
            model_name='order',
            name='supper1',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Polévka 1'),
        ),
        migrations.AlterField(
            model_name='order',
            name='supper2',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Polévka 2'),
        ),
    ]
