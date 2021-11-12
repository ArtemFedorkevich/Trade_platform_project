from django.db import models

from django.conf import settings


class StockBase(models.Model):
    """Base"""
    code = models.CharField("Code", max_length=8, unique=True)
    name = models.CharField("Name", max_length=128, unique=True)

    class Meta:
        abstract = True


class Currency(StockBase):

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"


class Item(StockBase):
    """Particular stock"""
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    currency = models.ForeignKey(Currency, blank=True, null=True, related_name='value', on_delete=models.SET_NULL)


class Inventory(models.Model):
    """The number of stocks a particular user has"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField("Stock quantity", default=0)

    class Meta:
        unique_together = [['user', 'item']]


class WatchList(models.Model):
    """Current user. Favorite list of stocks"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = [['user', 'item']]


class Money(models.Model):
    """Table of users money"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    money = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = [['user', 'money']]
