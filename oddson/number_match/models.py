import random

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from picklefield.fields import PickledObjectField


class Attempt(models.Model):
    """(Attempt description)"""
    contract = models.ForeignKey('Contract')
    user_number = models.PositiveIntegerField(_('user number'))
    our_number = models.PositiveIntegerField(_('our number'))

    # Log data
    ip_addr = models.GenericIPAddressField()
    request = PickledObjectField(_('request headers'))
    creation_date = models.DateTimeField(_('created'), auto_now_add=True)

    class Meta:
        verbose_name = _('attempt')
        verbose_name_plural = _('attempts')

    def __unicode__(self):
        return u'%s (%d)' % (self.contract, self.pk)

    def is_match(self):
        return self.user_number == self.our_number
    is_match.boolean = True

    # @models.permalink
    # def get_absolute_url(self):
    #     return ('number_match:attempt_detail', (), {'contract_id': self.contract_id, 'id': self.pk})


class Contract(models.Model):
    """(Contract description)"""
    is_active = models.BooleanField(_('active'), default=True)
    contract_id = models.SlugField(_('contract number'))
    compleation_date = models.DateTimeField(_('compleation date'), blank=True, null=True)
    creation_date = models.DateTimeField(_('created'), auto_now_add=True)

    # Date
    start_date = models.DateField(_('start date'), default=timezone.now)
    end_date = models.DateField(_('end date'))

    # Attempts
    allowed_attempts = models.PositiveIntegerField(_('allowed attempts'))
    used_attempts = models.PositiveIntegerField(_('used attempts'), default=0)

    # Range
    min_value = models.PositiveIntegerField(_('min value'), default=1)
    max_value = models.PositiveIntegerField(_('max value'))

    class Meta:
        verbose_name = _('contract')
        verbose_name_plural = _('contracts')

    def __unicode__(self):
        return self.contract_id

    def generate_number(self):
        return random.randint(self.min_value, self.max_value)

    # @models.permalink
    # def get_absolute_url(self):
    #     return ('number_match:contract_detail', (), {'id': self.pk})
