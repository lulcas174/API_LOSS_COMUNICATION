from django.db import models

from comunicacao_perda.farming_localization.models import FarmingLocalization


class Farming(models.Model):
    EXCESSIVE_RAN = 'EXCESSIVE_RAN'
    FROST = 'FROST'
    HAILSTORM = 'HAILSTORM'
    BARREN = 'BARREN'
    WINDSTORM = 'WINDSTORM'
    BOLT = 'BOLT'
    
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
