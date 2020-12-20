from django.contrib.auth.models import User
from django.db import models


class Food(models.Model):
    WARM_DRINKS = 0
    FIZZY_DRINKS = 1
    BEER = 2
    LIQUOR = 3
    SALADS = 4
    STUDENI_MEZETA = 5
    TOPLI_MEZETA = 6
    MEAT = 7
    SACHOVE = 8
    NUTS = 9

    FOOD_TYPES = (
        (WARM_DRINKS, 'Топли напитки'),
        (FIZZY_DRINKS, 'Безалкохолни напитки'),
        (BEER, 'Пиво'),
        (LIQUOR, 'Твърд алкохол'),
        (SALADS, 'Салати'),
        (STUDENI_MEZETA, 'Студени мезета'),
        (TOPLI_MEZETA, 'Топли мезета'),
        (MEAT, 'Скара'),
        (SACHOVE, 'Сачове'),
        (NUTS, 'Ядки')
    )

    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='food_images')
    weight = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    prep_time = models.IntegerField(default=0)
    type = models.IntegerField(choices=FOOD_TYPES)
    available = models.BooleanField(default=True)
    description = models.TextField()

    submitter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
