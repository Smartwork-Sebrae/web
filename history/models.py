# coding=utf-8
from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models


class History(models.Model):
    start = models.DateTimeField(_('Início'))
    end = models.DateTimeField(_('Fim'), null=True, blank=True)

    # relations
    order_desk = models.ForeignKey(
        to='order.OrderDesk', related_name='history')

    class Meta:
        verbose_name = _(u'Order Desk History')
        verbose_name_plural = _(u'Order Desk History')