# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.db import models


class Order(models.Model):
    CREATED = 'created'
    STARTED = 'started'
    STOPED = 'stoped'
    FINISHED = 'finished'
    STATUS_CHOICES = (
        (CREATED, 'Criada'),
        (STARTED, 'Iniciada'),
        (STOPED, 'Pausada'),
        (FINISHED, 'Terminada'),
    )
    quantity = models.IntegerField(_('Quantidade'))
    deadline = models.IntegerField(_('Prazo (dias)'))
    status = models.CharField(
        _('Status'), max_length=20, choices=STATUS_CHOICES,
        default=STARTED, blank=True)

    # relations
    item = models.ForeignKey(
        to='item.Item', related_name='orders',
        null=True, blank=True)
    desks = models.ManyToManyField(
        to='desk.Desk', through='order.OrderDesk',
        blank=True, related_name='orders',
        verbose_name='Estações de Trabalho')

    class Meta:
        verbose_name = _(u'Order')
        verbose_name_plural = _(u'Orders')

    def __unicode__(self):
        return self.item.name

    def get_absolute_url(self):
        return reverse('order:detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('order:update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('order:delete', kwargs={'pk': self.pk})

    def get_item_per_desk(self):
        return self.quantity // self.order_desks.count()

    def get_item_per_day(self):
        return self.get_item_per_desk() // self.deadline

    def get_left_items(self):
        return self.quantity - (self.quantity * 0.8)


class OrderDesk(models.Model):
    order = models.ForeignKey(to='order.Order', related_name='order_desks')
    desk = models.ForeignKey(to='desk.Desk', related_name='order_desks')

    class Meta:
        verbose_name = _(u'Order Desk')
        verbose_name_plural = _(u'Order Desks')

    @property
    def status(self):
        history = self.last_history
        if not history:
            return 'inactive'
        elif history.start and not history.end:
            return 'working'
        return 'idle'

    @property
    def get_status_display(self):
        return {
            'inactive': 'Inativa',
            'working': 'Em Atividade',
            'idle': 'Ociosa',
        }.get(self.status)
        # history = self.last_history
        # if not history:
        #     return 'Inativa'

        # if history.start and not history.end:
        #     return 'Em atividade'
        # else:
        #     return 'Ocioso'

    @property
    def last_history(self):
        return self.histories.last()
