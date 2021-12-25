from rest_framework import serializers
from comunicacao_perda.producer.models import FarmingProducer


class FarmingProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmingProducer
        fields = '__all__'
