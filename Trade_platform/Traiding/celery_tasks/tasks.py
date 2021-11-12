from Trade_platform.celery import app

from Traiding.models import Offer

from Items.models import Money

from Traiding.celery_tasks.get_transactions import get_transactions_list

from Traiding.celery_tasks.update_transactions import update_data


@app.task
def make_deal():
    # Get all active buy offers
    offer_buy_queryset = Offer.objects.filter(order_type=1, is_active=1)

    for buy_object in offer_buy_queryset:
        # Will check shell_offers from the cheapest stocks (order_by("price")),
        # and price lower than buyer price (price_lte=buy_object.price)
        offer_sell_queryset = Offer.objects.filter(
            order_type=2, is_active=1, price__lte=buy_object.price, item_id=buy_object.item_id
            ).order_by("price")
        money_queryset = Money.objects.get(user=buy_object.user_id)

        # get_transactions_list - return [] if user doesn't have enough money,
        # or list with details about transaction if deal can be made
        transactions_list = get_transactions_list(buy_object, offer_sell_queryset, money_queryset)

        # This function update all fields in database, and make transactions
        update_data(transactions_list)
