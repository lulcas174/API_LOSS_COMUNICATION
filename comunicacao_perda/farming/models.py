from django.db import models

from comunicacao_perda.farming_localization.models import FarmingLocalization


class Farming(models.Model):
    EXCESSIVE_RAN = 1
    FROST = 2
    HAILSTORM = 3
    BARREN = 4
    WINDSTORM = 5
    BOLT = 6
    
    TYPE_EVENT = (
        (EXCESSIVE_RAN, 'Chuva Excessiva'),
        (FROST, 'Geada'),
        (HAILSTORM, 'Granizo'),
        (BARREN, 'Seca'),
        (WINDSTORM, 'Vendaval'),
        (BOLT, 'Raio')
    )

    type_farming = models.CharField(max_length=100)
    farming_localization = models.ForeignKey(FarmingLocalization, on_delete=models.CASCADE)
    farming_event = models.CharField(max_length=20, choices=TYPE_EVENT)
    date_harvest = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.type_farming
