from django.db import models


class FarmingLocalization(models.Model):
    cep = models.CharField(max_length=9)
    street = models.CharField(max_length=255)
    complement = models.CharField(max_length=255)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    federative_unit = models.CharField(max_length=5)

    def __str__(self):
        return self.city
