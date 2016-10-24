# coding=utf-8
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from manager.forms import ManagerForm
from manager.models import Manager
from django.utils.translation import ugettext as _

from vanilla import model_views as views


class BaseManagerView():
    model = Manager
    form_class = ManagerForm
    lookup_field = 'pk'


class ManagerList(BaseManagerView, views.ListView):
    template_name = 'manager/list.html'
    page_title = _(u'Produções')


class ManagerCreate(BaseManagerView, views.CreateView):
    template_name = 'manager/form.html'


class ManagerDetail(BaseManagerView, views.DetailView):
    template_name = 'manager/detail.html'


class ManagerUpdate(BaseManagerView, views.UpdateView):
    template_name = 'manager/form.html'


class ManagerDelete(BaseManagerView, views.DeleteView):
    template_name = 'manager/delete.html'

    def get_success_url(self):
        return reverse('manager:list')
