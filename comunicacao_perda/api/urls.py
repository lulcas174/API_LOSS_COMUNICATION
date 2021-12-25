from django.urls import include, path
from rest_framework.routers import DefaultRouter

from comunicacao_perda.api.farming.views import FarmingView
from comunicacao_perda.api.farming_localization.views import FarmingLocalizationView
from comunicacao_perda.api.producer.views import FarmingProducerView

router = DefaultRouter()
router.register('producer', FarmingProducerView)
router.register('farming-localization', FarmingLocalizationView)
router.register('farming', FarmingView)

urlpatterns = [
    path('', include(router.urls))
]
