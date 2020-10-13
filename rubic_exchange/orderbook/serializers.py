from rest_framework import serializers

from rubic_exchange.orderbook.models import OrderBook


class OrderBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBook
        fields = '__all__'
