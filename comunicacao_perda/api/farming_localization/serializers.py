from rest_framework import serializers

from comunicacao_perda.farming_localization.models import FarmingLocalization


class FarmingLocalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmingLocalization
        fields = '__all__'
