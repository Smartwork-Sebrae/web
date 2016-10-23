from django.db.models import Q, Count
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

from vanilla import TemplateView


from desk.models import Desk
from order.models import OrderDesk, Order
from history.models import History


def now():
    return timezone.localtime(timezone.now())


class HistoryApiStart(APIView):
    def post(self, request, pk):
        order_desk = OrderDesk.objects.get(
            desk__pk=pk, order__status=Order.STARTED)
        History.objects.create(start=now(), order_desk=order_desk)
        return Response({})


class HistoryApiFinish(APIView):
    def post(self, request, pk):
        order_desk = OrderDesk.objects.get(
            desk__pk=pk, order__status=Order.STARTED)
        history = History.objects.filter(
            order_desk=order_desk
        ).last()
        history.end = now()
        history.save()

        desk = Desk.objects.get(pk=pk)
        if desk.is_last_desk:
            order = Order.objects.get(pk=order_desk.order.pk)
            if order.items_produced:
                order.items_produced += 1
            else:
                order.items_produced = 0
            order.save()

        return Response({})


class ApiDashboard(APIView):
    def get(self, request):
        orders = Order.objects.filter(status=Order.STARTED)
        started_desks = 0
        idle_desks = 0
        inactive_desks = 0
        desks = OrderDesk.objects.filter(
            order__pk__in=orders.values_list('pk', flat=True))
        desk_list = []
        for desk in desks:
            if desk.status == "working":
                started_desks += 1
            if desk.status == "idle":
                idle_desks += 1
            else:
                inactive_desks += 1

            end = start = None
            if desk.last_history:
                start = desk.last_history.start
                end = desk.last_history.end

            dic_desk = {
                "pk": desk.pk,
                "desk_number": desk.desk.number,
                "start": start.isoformat() if start else None,
                "finish": end.isoformat() if end else None,
                "status": desk.status,
                "formatted_status": desk.get_status_display,
                "order": desk.order_id
            }
            desk_list.append(dic_desk)

        return Response({
            "order_count": orders.count(),
            "total_left": 1200 - 160,
            "started_desk": started_desks,
            "idle_desk": idle_desks,
            "inactive_desk": inactive_desks,
            "total_desk": (
                started_desks + idle_desks + inactive_desks
            ),
            "desks": desk_list
        })

class ApiOrderProductivity(APIView):
    def get(self, request, pk):
        order = Order.objects.get(pk=pk)

        extra_args = {
            'date': 'history_history.end::timestamp::date'
        }
        db_engine = settings.DATABASES.get('default').get('ENGINE')
        if db_engine.endswith('sqlite3'):
            extra_args.update({
                'date': 'date(end)'
            })

        histories = History.objects.filter(
            Q(end__isnull=False) &
            Q(order_desk__order=order) &
            Q(order_desk__desk__next_desk__isnull=True) &
            Q(order_desk__desk__previous_desk__isnull=False)
        ).extra(select=extra_args).values('date').annotate(total=Count('id'))

        def accumulate_total(histories):
            total = 0
            for x in histories:
                total += x
                yield total

        return Response({
            'pk': order.pk,
            'item': order.item.name,
            'deadline': order.deadline,
            'quantity': order.quantity,
            'histories': accumulate_total(
                [history.get('total') for history in histories]
            ),
        })


class DashboardView(TemplateView):
    template_name = 'history/dashboard.html'


class OrderProductivityView(TemplateView):
    template_name = 'history/order_productivity.html'

    def get_context_data(self, **kwargs):
        context = super(OrderProductivityView, self).get_context_data(**kwargs)
        context.update(
            orders=Order.objects.all()
        )
        return context
