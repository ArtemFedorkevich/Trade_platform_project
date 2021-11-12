from Traiding.models import Trade, Offer

from Items.models import Inventory, Money

from django.db.models import F


def update_data(transaction_list):
    for item in transaction_list:
        # Make transaction
        Trade.objects.create(quantity=item[0], unit_price=item[1], description=item[2],
                             buyer_id=item[3], buyer_offer_id=item[4], item_id=item[5], seller_id=item[6],
                             seller_offer_id=item[7])

        # Update information about buyer
        Offer.objects.filter(id=item[4]).update(entry_quantity=F('entry_quantity')-item[0])
        Inventory.objects.filter(user_id=item[3], item_id=item[5]).update(quantity=F('quantity') + item[0])
        Money.objects.filter(user_id=item[3]).update(money=F('money') - item[1]*item[0])

        query_buyer = Offer.objects.get(id=item[4])
        # Check amount of stocks in database (if 0 - offer become inactive)
        if query_buyer.entry_quantity == 0:
            query_buyer.is_active = 0
            query_buyer.save()

        # Update information about seller
        Offer.objects.filter(id=item[7]).update(entry_quantity=F('entry_quantity') - item[0])
        Inventory.objects.filter(user_id=item[6], item_id=item[5]).update(quantity=F('quantity') - item[0])
        Money.objects.filter(user_id=item[6]).update(money=F('money') + item[1] * item[0])

        query_seller = Offer.objects.get(id=item[7])
        if query_seller.entry_quantity == 0:
            query_seller.is_active = 0
            query_seller.save()
