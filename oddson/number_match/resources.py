from djangorestframework.resources import ModelResource
from djangorestframework.reverse import reverse

from .models import Attempt, Contract


class AttemptResource(ModelResource):
    exclude = ('pk', 'contract', 'ip_addr', 'request')
    include = ('resources', 'url', 'is_match')
    model = Attempt

    def resources(self, instance):
        return {
            'contract': reverse('number_match:contract_detail', kwargs={
                'id': instance.contract_id
            }, request=self.request),
        }

    def url(self, instance):
        return reverse('number_match:attempt_detail', kwargs={
            'contract_id': instance.contract_id,
            'id': instance.pk
        }, request=self.request)


class ContractResource(ModelResource):
    exclude = ('pk', 'creation_date', 'is_active')
    include = ('resources', 'url')
    model = Contract

    def resources(self, instance):
        return {
            'attempts': reverse('number_match:attempt_list', kwargs={
                'contract_id': instance.pk
            }, request=self.request),
        }

    def url(self, instance):
        return reverse('number_match:contract_detail', kwargs={
            'id': instance.pk
        }, request=self.request)
