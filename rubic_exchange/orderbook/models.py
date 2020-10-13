from django.db import models
from django.utils import timezone


from rubic_exchange.consts import MAX_WEI_DIGITS


class Network(models.Model):
    name = models.CharField(max_length=128, db_index=True)


class OrderContractId(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class OrderBook(models.Model):
    order_contract = models.OneToOneField(OrderContractId, on_delete=models.CASCADE)
    network = models.ForeignKey(Network, on_delete=models.CASCADE, default=1)

    owner_address = models.CharField(max_length=50)
    base_address = models.CharField(max_length=50)
    quote_address = models.CharField(max_length=50)

    base_limit = models.DecimalField(max_digits=MAX_WEI_DIGITS, decimal_places=0)
    quote_limit = models.DecimalField(max_digits=MAX_WEI_DIGITS, decimal_places=0)
    expiration_timestamp = models.BigIntegerField()
    base_only_investor = models.CharField(max_length=50)
    min_base_investment = models.DecimalField(max_digits=MAX_WEI_DIGITS, decimal_places=0)
    min_quote_investment = models.DecimalField(max_digits=MAX_WEI_DIGITS, decimal_places=0)
    broker_address = models.CharField(max_length=50)
    broker_base_percent = models.IntegerField()
    broker_quote_percent = models.IntegerField()
    refund_delay_seconds = models.BigIntegerField()
    public = models.BooleanField(default=True)

    state = models.CharField(max_length=63, default='CREATED')

    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    state_changed_at = models.DateTimeField(default=timezone.now)
