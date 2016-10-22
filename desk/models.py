from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.db import models


class Desk(models.Model):
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

    name = models.CharField(_('Nome'), max_length=200)
    number = models.CharField(_('Numero'), max_length=200)
    status = models.CharField(
        _('Status'), max_length=20, choices=STATUS_CHOICES,
        default=CREATED, blank=True)

    class Meta:
        verbose_name = _(u'Desk')
        verbose_name_plural = _(u'Desks')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('desk:detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('desk:update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('desk:delete', kwargs={'pk': self.pk})
