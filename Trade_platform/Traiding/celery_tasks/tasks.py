from Trade_platform.celery import app

from Traiding.models import Offer

from Items.models import Money

from Traiding.celery_tasks.get_transactions import get_transactions_list

@app.task
def make_deal():
    offer_buy_queryset = Offer.objects.filter(order_type=1, is_active=1)

    for buy_object in offer_buy_queryset:
        # We will check shell_offers from the cheapest stocks, and price lower than buyer price
        offer_sell_queryset = Offer.objects.filter(
            order_type=2, is_active=1, price__lte=buy_object.price, item_id = buy_object.item_id
            ).order_by("price")
        money_queryset = Money.objects.get(user=buy_object.user_id)

        print(get_transactions_list(buy_object, offer_sell_queryset, money_queryset))


