# Generated by Django 4.0.4 on 2022-06-23 13:48

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('description', models.TextField(blank=True, default='', verbose_name='Описание')),
                ('self', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='service', to='chess_spreadsheet.service')),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('description', models.TextField(blank=True, default='', verbose_name='Описание')),
                ('self', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='object', to='chess_spreadsheet.object')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('self', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='client', to='chess_spreadsheet.client')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'Новая бронь'), ('2', 'Ожидание клиента'), ('3', 'Клиент приехал'), ('4', 'Клиент уехал'), ('5', 'Отмена')], default='1', max_length=20)),
                ('customers_count', models.IntegerField(default=1, verbose_name='Количество посетителей')),
                ('date', models.DateField(verbose_name='Дата брони')),
                ('time_from', models.TimeField(verbose_name='Время начала брони')),
                ('time_to', models.TimeField(verbose_name='Время конца брони')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата бронирования')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='booking', to='chess_spreadsheet.client', verbose_name='Клиент')),
                ('object', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking', to='chess_spreadsheet.object', verbose_name='Объект')),
                ('self', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='booking', to='chess_spreadsheet.booking')),
                ('services', models.ManyToManyField(blank=True, related_name='booking', to='chess_spreadsheet.service', verbose_name='Доп. услуги')),
            ],
        ),
    ]
