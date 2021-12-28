from comunicacao_perda.farming_localization.models import FarmingLocalization


class farmingLocalizationRepository(object):
    @staticmethod
    def filter(**kwargs):
        return FarmingLocalization.objects.filter(**kwargs)

    @staticmethod
    def crate_farming_localization(farmingLocalization: FarmingLocalization, data):
        farmingLocalization.cep = data.get('cep')
        farmingLocalization.street = data.get('street')
        farmingLocalization.complement = data.get('complement')
        farmingLocalization.district = data.get('district')
        farmingLocalization.city = data.get('city')
        farmingLocalization.federative_unit = data.get('federative_unit')
        farmingLocalization.save()