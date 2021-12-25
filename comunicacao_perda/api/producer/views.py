import json

from django.core.exceptions import FieldError
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from comunicacao_perda.api.producer.serializers import FarmingProducerSerializer
from comunicacao_perda.producer.models import FarmingProducer
from comunicacao_perda.producer.repositories import ProducerRepository


class FarmingProducerView(ModelViewSet):
    queryset = FarmingProducer.objects.all()
    serializer_class = FarmingProducerSerializer

    def create(self, request, *args, **kwargs):
        try:
            message = self._validate_create(request.data)

            if message:
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

            farmingProducer = FarmingProducer()
            ProducerRepository.create_farming_producer(farmingProducer, request.data)

        except Exception:
            return Response(
                'Houve um problema ao criar o produto rural.',
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        return Response(
            FarmingProducerSerializer(farmingProducer).data,
            status=status.HTTP_201_CREATED
        )
    def _validate_create(self, data):
        if data.get('name_producer') is None:
            return 'É necessário informar um nome de produtor rural válido.'
        try:
           str(data.get('name_producer'))
        except:
            return 'É necessário informar o nome do produtor válido.'
       

        if data.get('cpf_producer') is None:
            return 'É necessário informar um CPF válido para o produtor rural.'
        try:
            int(data.get('cpf_producer'))
        except FieldError:
            return 'É necessário informar um tipo válido para o CPF'
