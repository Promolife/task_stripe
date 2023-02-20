from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.


class Discount(models.Model):
    name = models.CharField(
        'Название скидки',
        max_length=100,
        help_text='Не более 100 символов'
    )
    description = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='Не более 100 символов'
    )
    amount = models.IntegerField(
        'Значение',
        default=0,
        help_text='Скидка на товар'
    )
    stripe_id = models.CharField(
        'ID Stripe',
        max_length=100,
        blank=True,
        null=True,
        help_text='Не более 100 символов'
    )

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
        ordering = ['-name']

    def __str__(self):
        return self.name[:20]


class Tax(models.Model):
    name = models.CharField(
        'Название налога',
        max_length=100,
        help_text='Не более 100 символов'
    )
    description = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='Не более 100 символов'
    )
    amount = models.IntegerField(
        'Значение',
        default=0,
        help_text='Налог на товар'
    )
    txr = models.CharField(
        'Hash',
        max_length=100,
        blank=True,
        null=True,
        help_text='Не более 100 символов'
    )

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'
        ordering = ['-name']

    def __str__(self):
        return self.name[:20]


class Item(models.Model):
    name = models.CharField(
        'Название товара',
        max_length=100,
        help_text='Не более 100 символов'
        )
    description = models.CharField(
        'Описание',
        max_length=250,
        blank=True,
        null=True,
        help_text='Не более 100 символов. Не обязательно'
        )
    price = models.IntegerField(
        'Цена',
        default=0,
        help_text='Цена на товар'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-name']

    def __str__(self):
        return self.name[:20]


class Order(models.Model):
    items = models.ManyToManyField(
        Item,
        through='ItemOrder',
        related_name='items'
    )
    description = models.TextField(
        'Описание',
        blank=True,
        null=True,
        help_text='Краткое описание заказа'
    )
    discount = models.ForeignKey(
        Discount,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='discount',
        verbose_name='Скидка'
    )
    tax = models.ForeignKey(
        Tax,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='tax',
        verbose_name='Налог'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-pk']

    def __str__(self):
        return self.description[:20]


class ItemOrder(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='itemsorder',
        verbose_name='Товар'
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='orderitems',
        verbose_name='Заказ'
    )
    created = models.DateTimeField(
        'Создан',
        auto_now_add=True
        )

    class Meta:
        verbose_name = 'Спискок товаров заказа'
        verbose_name_plural = 'Списки товаров в заказах'
