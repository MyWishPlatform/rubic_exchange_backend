from rest_framework.exceptions import ValidationError

from rubic_exchange.orderbook.models import OrderContractId, OrderBook
from rubic_exchange.orderbook.serializers import OrderBookSerializer


def make_new_id():
    order_contract = OrderContractId()
    order_contract.save()
    return order_contract.id
