from rest_framework.viewsets import ModelViewSet

from comunicacao_perda.api.producer.serializers import FarmingProducerSerializer
from comunicacao_perda.producer.models import FarmingProducer


class FarmingProducerView(ModelViewSet):
    queryset = FarmingProducer.objects.all()
    serializer_class = FarmingProducerSerializer
