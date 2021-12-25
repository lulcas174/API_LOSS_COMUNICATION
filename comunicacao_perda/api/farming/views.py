from rest_framework.viewsets import ModelViewSet

from comunicacao_perda.api.farming.serializers import FarmingSerializer
from comunicacao_perda.farming.models import Farming


class FarmingView(ModelViewSet):
    queryset = Farming.objects.all()
    serializer_class = FarmingSerializer
