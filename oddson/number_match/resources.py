from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource

from .models import Attempt, Contract


class AttemptResource(ModelResource):
    exclude = ('id', 'pk', 'contract', 'ip_addr', 'request')
    include = ('contract_uri', 'resource_uri', 'is_match')
    model = Attempt

    def contract_uri(self, instance):
        return reverse('number_match:contract_detail', kwargs={'id': instance.contract_id})

    def resource_uri(self, instance):
        return reverse('number_match:attempt_detail', kwargs={'contract_id': instance.contract_id, 'id': instance.pk})


class ContractResource(ModelResource):
    exclude = ('id', 'pk', 'creation_date', 'is_active')
    include = ('attempt_uri', 'resource_uri')
    model = Contract

    def attempt_uri(self, instance):
        return reverse('number_match:attempt_list', kwargs={'contract_id': instance.pk})

    def resource_uri(self, instance):
        return reverse('number_match:contract_detail', kwargs={'id': instance.pk})
