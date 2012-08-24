from django.core.urlresolvers import reverse
from djangorestframework.views import (
    InstanceModelView, ListModelView, ListOrCreateModelView, View
)

from .resources import AttemptResource, ContractResource


class AttemptListView(ListOrCreateModelView):
    resource = AttemptResource


class AttemptView(InstanceModelView):
    resource = AttemptResource


class ContractListView(ListModelView):
    resource = ContractResource


class ContractView(InstanceModelView):
    resource = ContractResource


class Resources(View):
    def get(self, request):
        return [
            {'name': 'Contract API', 'resource_uri': reverse('number_match:contract_list')}
        ]
