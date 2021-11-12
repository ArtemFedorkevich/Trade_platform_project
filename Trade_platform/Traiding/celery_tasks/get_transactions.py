def get_transactions_list(buy_object, offer_sell_queryset, money_queryset):

    current_stocks = 0
    buy_price = 0
    deal_data = []

    for sell_object in offer_sell_queryset:
        # We can buy stocks from many owners, current stocks collect amount of stocks from different owners.
        if current_stocks + sell_object.entry_quantity < buy_object.entry_quantity:
            current_stocks += sell_object.entry_quantity
            buy_price += sell_object.entry_quantity * sell_object.price

            # Collect all data for make note in database (Trade table)
            deal_data.append((sell_object.entry_quantity, float(sell_object.price),
                              f"Transaction complete.\n Amount of bought stocks: {buy_object.entry_quantity}",
                              buy_object.user_id, buy_object.id, buy_object.item_id,
                              sell_object.user_id, sell_object.id))
        # This block is executed when the buyer find final owner who sell stocks.
        # last_trade_stocks not equal final owner stocks because owner can have more stocks than buyer need
        # example : current_stocks = 30, buyer need 10 stocks (entry_quantity = 40),
        # final owner have 50 stocks, as result last_trade_stocks = 10, not 40
        else:
            buy_price += (buy_object.entry_quantity - current_stocks) * sell_object.price
            if buy_price <= money_queryset.money:
                last_trade_stocks = buy_object.entry_quantity - current_stocks
                deal_data.append((last_trade_stocks, float(sell_object.price),
                                  f"Transaction complete.\n Amount of bought stocks: {buy_object.entry_quantity}",
                                  buy_object.user_id, buy_object.id, buy_object.item_id,
                                  sell_object.user_id, sell_object.id))
                break
            # If buyer doesn't have enough money deal rejected(deal_data = [])
            else:
                deal_data = []
                break
    # This block is executed when amount of sold stocks in market less than buyer entry_quantity,
    # as result exit from for cycle was "natural"
    else:
        if buy_price > money_queryset.money:
            deal_data = []

    return deal_data
