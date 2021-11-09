from django.contrib.auth.models import User

from django.db import models

from Items.models import Item

from django.conf import settings


class Offer(models.Model):
    """Request to buy or sell specific stocks"""
    OrderType = [('1', 'buy'), ('2', 'sell')]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)
    entry_quantity = models.IntegerField("Requested quantity")
    order_type = models.PositiveSmallIntegerField(choices=OrderType)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    is_active = models.BooleanField(default=True)

class Trade(models.Model):
    """Information about a certain transaction"""
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)
    seller = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='seller_trade',
        related_query_name='seller_trade',
    )
    buyer = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='buyer_trade',
        related_query_name='buyer_trade',
    )
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    buyer_offer = models.ForeignKey(
        Offer,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='buyer_trade',
        related_query_name='buyer_trade',
    )
    seller_offer=models.ForeignKey(
        Offer,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='seller_trade',
        related_query_name='seller_trade',
    )