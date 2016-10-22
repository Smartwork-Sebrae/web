from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response

from order.models import OrderDesk, Order
from history.models import History


class HistoryApiStart(APIView):
    def post(self, request, pk):
        order_desk = OrderDesk.objects.get(
            desk__pk=pk, order__status=Order.STARTED)
        History.objects.create(start=timezone.now(), order_desk=order_desk)
        return Response({})


class HistoryApiFinish(APIView):
    def post(self, request, pk):
        order_desk = OrderDesk.objects.get(
            desk__pk=pk, order__status=Order.STARTED)
        history = History.objects.get(order_desk=order_desk)
        history.end = timezone.now()
        history.save()
        return Response({})


class ApiDashboard(APIView):
    def get(self, request):
        orders = Order.objects.filter(status=Order.STARTED)
        started_desks = 0
        idle_desks = 0
        desks = OrderDesk.objects.filter(order__pk__in=orders.values_list("pk", flat=True))
        desk_list = []
        for desk in desks:
            if desk.status == "idle":
                idle_desks += 1
            else:
                started_desks += 1

            dic_desk = {
                "pk": desk.pk,
                "start": desk.last_history.start if desk.last_history else None,
                "finish": desk.last_history.end if desk.last_history else None,
                "status": desk.status,
                "order":  desk.order_id
            }
            desk_list.append(dic_desk)

        return Response({
            "order_count": orders.count(),
            "started_desk": started_desks,
            "idle_desk": idle_desks,
            "desks": desk_list
        })
