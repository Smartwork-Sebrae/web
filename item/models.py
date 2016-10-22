from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.db import models


class Item(models.Model):
    name = models.CharField(_('Nome'), max_length=200)
    estimated_time = models.FloatField(_('Tempo estimado'))

    class Meta:
        verbose_name = _(u'Item')
        verbose_name_plural = _(u'Items')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item:detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('item:update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('item:delete', kwargs={'pk': self.pk})
