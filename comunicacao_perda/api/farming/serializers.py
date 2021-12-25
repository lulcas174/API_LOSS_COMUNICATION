from rest_framework import serializers
from comunicacao_perda.farming.models import Farming


class FarmingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farming
        fields = '__all__'
