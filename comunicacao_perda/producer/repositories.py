from comunicacao_perda.producer.models import FarmingProducer


class ProducerRepository(object):
    @staticmethod
    def filter(**kwargs):
        return FarmingProducer.objects.filter(**kwargs)

    @staticmethod
    def create_farming_producer(farmingProducer: FarmingProducer, data):
        farmingProducer.name_productor = data.get('name_producer')
        farmingProducer.email = data.get('email')
        farmingProducer.cpf_producer = int(data.get('cpf_producer'))
        farmingProducer.save()
