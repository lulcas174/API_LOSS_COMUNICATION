from django.db import models


class FarmingProducer(models.Model):
    name_productor = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, blank=True, null=True)
    cpf_producer = models.IntegerField()

    def __str__(self):
        return self.name_productor
