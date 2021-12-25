from django.contrib import admin

from comunicacao_perda.farming.models import Farming
from comunicacao_perda.farming_localization.models import FarmingLocalization
from comunicacao_perda.producer.models import FarmingProducer

admin.site.register(FarmingLocalization)
admin.site.register(Farming)
admin.site.register(FarmingProducer)