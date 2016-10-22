from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from order.forms import OrderForm

from vanilla import model_views as views

from order.models import Order, OrderDesk


class BaseOrderView():
    model = Order
    form_class = OrderForm
    lookup_field = 'pk'


class OrderList(BaseOrderView, views.ListView):
    template_name = 'order/list.html'
    page_title = _(u'Orders')


class OrderCreate(BaseOrderView, views.CreateView):
    template_name = 'order/form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        for desk in form.cleaned_data.get('desks'):
            OrderDesk.objects.create(
                order=self.object,
                desk=desk,
            )

        return HttpResponseRedirect(self.get_success_url())


class OrderDetail(BaseOrderView, views.DetailView):
    template_name = 'order/detail.html'


class OrderUpdate(BaseOrderView, views.UpdateView):
    template_name = 'order/form.html'

    def form_valid(self, form):
        desks = form.cleaned_data.get('desks')
        self.object = form.save(commit=False)
        self.object.save()
        self.object.order_desks.exclude(
            desk__id__in=desks.values_list('pk', flat=True)
        ).delete()
        for desk in desks:
            OrderDesk.objects.get_or_create(
                order=self.object,
                desk=desk,
            )

        return HttpResponseRedirect(self.get_success_url())




class OrderDelete(BaseOrderView, views.DeleteView):
    template_name = 'order/delete.html'

    def get_success_url(self):
        return reverse('order:list')
