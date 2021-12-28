from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from comunicacao_perda.api.farming_localization.serializers import FarmingLocalizationSerializer
from comunicacao_perda.farming_localization.models import FarmingLocalization
from comunicacao_perda.farming_localization.repositories import farmingLocalizationRepository


class FarmingLocalizationView(ModelViewSet):
    queryset = FarmingLocalization.objects.all()
    serializer_class = FarmingLocalizationSerializer

    def create(self, request, *args, **kwargs):
        try:
            message = self._validate_length_cep(request.data)

            if message:
                return Response(
                    message,
                    status=status.HTTP_400_BAD_REQUEST
                )

            farmingLocalization = FarmingLocalization()
            farmingLocalizationRepository.crate_farming_localization(farmingLocalization, request.data)

        except Exception:
            return Response(
                'Houve um problema ao registrar a localização da lavoura',
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            FarmingLocalizationSerializer(farmingLocalization).data,
            status=status.HTTP_201_CREATED
        )

    def _validate_length_cep(self, data):
        if data.get('cep') is None:
            return 'É necessário um CEP válido.'
        if len(data.get('cep')) != 8:
            return 'O cep tem um tamanho inválido.'
