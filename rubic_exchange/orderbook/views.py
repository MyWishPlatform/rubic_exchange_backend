from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import NotFound
from rest_framework import mixins

from rubic_exchange.orderbook.api import make_new_id
from rubic_exchange.orderbook.models import OrderBook
from rubic_exchange.orderbook.serializers import OrderBookSerializer


@api_view(http_method_names=['GET'])
def generate_order_id(request: Request):
    order_id = make_new_id()
    return Response({'id': order_id})


class OrderBookViewSet(mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    queryset = OrderBook.objects.filter(public=True)
    serializer_class = OrderBookSerializer
    permission_classes = []

    def retrieve(self, request: Request, *args, **kwargs):
        order_id = kwargs.get('pk')
        try:
            order = OrderBook.objects.get(order_contract__id=order_id)
        except OrderBook.DoesNotExist:
            raise NotFound

        serializer = self.get_serializer(order)
        return Response(serializer.data)
