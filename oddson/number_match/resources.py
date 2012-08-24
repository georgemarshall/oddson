from djangorestframework.resources import ModelResource
from djangorestframework.reverse import reverse

from .forms import AttemptForm
from .models import Attempt, Game


class AttemptResource(ModelResource):
    exclude = ('pk', 'ip_addr', 'request')
    include = ('resources', 'url', 'is_match')
    model = Attempt
    form = AttemptForm

    def resources(self, instance):
        return {
            'game': reverse('number_match:detail', kwargs={
                'id': instance.game_id
            }, request=self.request),
        }

    def url(self, instance):
        return reverse('number_match:attempt_detail', kwargs={
            'game_id': instance.game_id,
            'id': instance.pk
        }, request=self.request)


class GameResource(ModelResource):
    exclude = ('pk', 'creation_date', 'is_active')
    include = ('resources', 'url')
    model = Game

    def resources(self, instance):
        return {
            'attempts': reverse('number_match:attempt_list', kwargs={
                'game_id': instance.pk
            }, request=self.request),
        }

    def url(self, instance):
        return reverse('number_match:detail', kwargs={
            'id': instance.pk
        }, request=self.request)
