from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from vanilla import model_views as views

from item.models import Item


class BaseItemView():
    model = Item
    lookup_field = 'pk'


class ItemList(BaseItemView, views.ListView):
    template_name = 'item/list.html'
    page_title = _(u'Items')


class ItemCreate(BaseItemView, views.CreateView):
    template_name = 'item/form.html'


class ItemDetail(BaseItemView, views.DetailView):
    template_name = 'item/detail.html'


class ItemUpdate(BaseItemView, views.UpdateView):
    template_name = 'item/form.html'


class ItemDelete(BaseItemView, views.DeleteView):
    template_name = 'item/delete.html'

    def get_success_url(self):
        return reverse('item:list')
