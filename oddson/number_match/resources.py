from djangorestframework.resources import ModelResource

from .models import Attempt, Contract


class AttemptResource(ModelResource):
    model = Attempt


class ContractResource(ModelResource):
    model = Contract
