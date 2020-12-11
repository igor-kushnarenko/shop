# -*- coding: utf-8 -*-

from django.db import models
from PIL import Image


class Products(models.Model):
	SWEATSHIRT = 'Свитшоты'
	SHIRT = 'Футболки'
	CAP = 'Шапочки'
	SUIT = 'Костюмчики'
	PANTS = 'Штанишки'
	SHORTS = 'Шортики'
	MALE = 'Мужской'
	FEMALE = 'Женский'

	TYPES = {
		(SWEATSHIRT, 'Свитшоты'),
		(SHIRT, 'Футболки'),
		(CAP, 'Шапочки'),
		(SUIT, 'Костюмчики'),
		(PANTS, 'Штанишки'),
		(SHORTS, 'Шортики'),
	}

	SEX = {
		(MALE, 'Мужской'),
		(FEMALE, 'Женский')
	}

	SIZE = {
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
	size = models.CharField('Размер', max_length=10, choices=SIZE)
	img = models.ImageField('Изображение', default='no_image.jpg', upload_to='product_image')


	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукция'


