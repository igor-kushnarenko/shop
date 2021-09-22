# -*- coding: utf-8 -*-

from django.db import models


class Products(models.Model):
    SWEATSHIRT = 'Свитшоты'
    SHIRT = 'Футболки'
    CAP = 'Шапки'
    SUIT = 'Костюмы'
    PANTS = 'Брюки'
    SKIRTS = 'Юбки'
    ACCESS = 'Аксессуары'
    MALE = 'Мужской'
    FEMALE = 'Женский'
    UNISEX = 'Унисекс'

    TYPES = {
        (SWEATSHIRT, 'Свитшоты'),
        (SHIRT, 'Футболки'),
        (CAP, 'Шапки'),
        (SUIT, 'Костюмы'),
        (PANTS, 'Брюки'),
        (SKIRTS, 'Юбки'),
        (ACCESS, 'Аксессуары')
    }

    SEX = {
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
        (UNISEX, 'Унисекс')
    }

    SIZE = {
        ('None', 'Не указан'),
        ('24-26', '24-26'),
        ('26-28', '26-28'),
        ('28-30', '28-30'),
    }

    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    price = models.IntegerField('Цена')
    avaliability = models.BooleanField('Наличие')
    group = models.CharField('Тип', max_length=20, choices=TYPES, default=SHIRT)
    sex = models.CharField('Пол', max_length=10, choices=SEX)
    size = models.CharField('Размер', max_length=10, choices=SIZE, default='None')
    img = models.ImageField('Изображение', default='no_image.jpg', upload_to='product_image', null=True, blank=True,
                            editable=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'
