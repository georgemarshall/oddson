from django.shortcuts import get_object_or_404
from djangorestframework import status
from djangorestframework.mixins import PaginatorMixin, ReadModelMixin
from djangorestframework.response import Response
from djangorestframework.reverse import reverse
from djangorestframework.views import (
    ListModelView, ModelView, View
)

from .resources import AttemptResource, GameResource


class AttemptListView(PaginatorMixin, ListModelView):
    resource = AttemptResource

    def post(self, request, *args, **kwargs):
        contract = get_object_or_404(GameResource.model, pk=kwargs['game_id'])

        instance = contract.attempt_set.create(
            our_number=contract.generate_number(),
            user_number=self.CONTENT['number'],
            ip_addr=request.META.get('REMOTE_ADDR'),
            request=dict(
                (k.replace('HTTP_', '').replace('_', '-').title(), v)
            for k, v in request.META.iteritems() if k.startswith('HTTP_'))
        )

        headers = {}
        if hasattr(self.resource, 'url'):
            headers['Location'] = self.resource(self).url(instance)
        return Response(status.HTTP_201_CREATED, instance, headers)


class AttemptView(ReadModelMixin, ModelView):
    resource = AttemptResource


class GameListView(PaginatorMixin, ListModelView):
    resource = GameResource


class GameView(ReadModelMixin, ModelView):
    resource = GameResource


class Resources(View):
    def get(self, request, *args, **kwargs):
        return {'resources': {
            'number_match': reverse('number_match:list', request=request)
        }}
