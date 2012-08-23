from djangorestframework.views import (
    ListModelView, ListOrCreateModelView, ModelView
)

from .resources import AttemptResource, ContractResource


class AttemptListView(ListOrCreateModelView):
    resource = AttemptResource


class AttemptView(ModelView):
    resource = AttemptResource


class ContractListView(ListModelView):
    resource = ContractResource


class ContractView(ModelView):
    resource = ContractResource
