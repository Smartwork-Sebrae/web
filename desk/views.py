from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from desk.forms import DeskForm

from vanilla import model_views as views

from desk.models import Desk


class BaseDeskView():
    model = Desk
    form_class = DeskForm
    lookup_field = 'pk'


class DeskList(BaseDeskView, views.ListView):
    template_name = 'desk/list.html'
    page_title = _(u'Desks')


class DeskCreate(BaseDeskView, views.CreateView):
    template_name = 'desk/form.html'


class DeskDetail(BaseDeskView, views.DetailView):
    template_name = 'desk/detail.html'


class DeskUpdate(BaseDeskView, views.UpdateView):
    template_name = 'desk/form.html'


class DeskDelete(BaseDeskView, views.DeleteView):
    template_name = 'desk/delete.html'

    def get_success_url(self):
        return reverse('desk:list')
