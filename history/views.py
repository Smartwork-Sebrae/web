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
