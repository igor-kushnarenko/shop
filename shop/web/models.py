from django.db import models


class Products(models.Model):
	SWEATSHIRT = 'Свитшоты'
	CAP = 'Шапочки'
	SUIT = 'Костюмчики'
	PANTS = 'Штанишки'
	SHORTS = 'Шортики'

	TYPES = {
		(SWEATSHIRT, 'Свитшоты'),
		(CAP, 'Шапочки'),
		(SUIT, 'Костюмчики'),
		(PANTS, 'Штанишки'),
		(SHORTS, 'Шортики'),
	}


	name = CharField('Name', max_length=50)

