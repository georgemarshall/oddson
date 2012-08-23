from djangorestframework.views import ListModelView, ModelView

from .resources import ContractResource


class ContractListView(ListModelView):
    resource = ContractResource


class ContractView(ModelView):
    resource = ContractResource
