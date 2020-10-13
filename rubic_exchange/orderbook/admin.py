from django.contrib import admin
from rubic_exchange.orderbook.models import OrderBook, OrderContractId, Network


admin.site.register(OrderBook)
admin.site.register(OrderContractId)
admin.site.register(Network)
