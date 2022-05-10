from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    name = models.CharField('Имя', max_length=200)
    phone_number = PhoneNumberField(
        unique=True,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        'Почта',
        null=True,
        blank=True
    )
    self = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        related_name='client',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Object(models.Model):
    title = models.CharField('Название', max_length=50)
    price = models.IntegerField('Цена')
    description = models.TextField('Описание', blank=True, default='')
    self = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        related_name='object',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.title} [{self.price} руб.]'


class Service(models.Model):
    title = models.CharField('Название', max_length=50)
    price = models.IntegerField('Цена')
    description = models.TextField('Описание', blank=True, default='')
    self = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        related_name='service',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.title} [{self.price} руб.]'


class Booking(models.Model):
    STATUS_CHOICES = [
        ('1', 'Новая бронь'),
        ('2', 'Ожидание клиента'),
        ('3', 'Клиент приехал'),
        ('4', 'Клиент уехал'),
        ('5', 'Отмена'),
    ]
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='1'
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        verbose_name='Клиент',
        related_name='booking'
    )
    customers_count = models.IntegerField(
        'Количество посетителей',
        default=1
    )
    object = models.ForeignKey(
        Object,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Объект',
        related_name='booking'
    )
    services = models.ManyToManyField(
        Service,
        verbose_name='Доп. услуги',
        related_name='booking',
        blank=True
    )
    date = models.DateField(
        'Дата брони'
    )
    time_from = models.TimeField(
        'Время начала брони'
    )
    time_to = models.TimeField(
        'Время конца брони'
    )
    pub_date = models.DateTimeField(
        'Дата бронирования',
        auto_now_add=True
    )
    self = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        related_name='booking',
        null=True,
        blank=True
    )

    def get_sum(self) -> int:
        res = int(self.object.price)
        for service in self.services.all():
            res += int(service.price)
        return res

    def __str__(self):
        return f'№{self.pk} {self.client} [{self.get_sum()} руб.]'
