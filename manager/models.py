# coding=utf-8
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.db import models


class Manager(models.Model):
    hour = models.TimeField(_('Hora'), max_length=10)
    produced = models.IntegerField(_('Peças produzidas'))

    # relations
    order = models.ForeignKey(
        to='order.Order', related_name='manager', null=True)

    class Meta:
        verbose_name = _(u'Manager')
        verbose_name_plural = _(u'Managers')

    def get_absolute_url(self):
        return reverse('manager:detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('manager:update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('manager:delete', kwargs={'pk': self.pk})
