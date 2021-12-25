from rest_framework.viewsets import ModelViewSet

from comunicacao_perda.api.farming_localization.serializers import FarmingLocalizationSerializer
from comunicacao_perda.farming_localization.models import FarmingLocalization


class FarmingLocalizationView(ModelViewSet):
    queryset = FarmingLocalization.objects.all()
    serializer_class = FarmingLocalizationSerializer
