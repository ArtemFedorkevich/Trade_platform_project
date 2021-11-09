def get_transactions_list(buy_object, offer_sell_queryset, money_queryset):
    current_stocks = 0
    buy_price = 0
    deal_data = []
    for sell_object in offer_sell_queryset:
        if current_stocks + sell_object.entry_quantity < buy_object.entry_quantity:
            current_stocks += sell_object.entry_quantity
            buy_price += sell_object.entry_quantity * sell_object.price
            deal_data.append((sell_object.entry_quantity, float(sell_object.price), "Transaction complete",
                              buy_object.user_id, buy_object.id, buy_object.item_id,
                              sell_object.user_id, sell_object.id))

        else:
            buy_price += (buy_object.entry_quantity - current_stocks) * sell_object.price
            if buy_price <= money_queryset.money:
                last_trade_stocks = buy_object.entry_quantity - current_stocks
                deal_data.append((last_trade_stocks, float(sell_object.price), "Transaction complete",
                                  buy_object.user_id, buy_object.id, buy_object.item_id,
                                  sell_object.user_id, sell_object.id))
                break
            else:
                last_trade_stocks = buy_object.entry_quantity - current_stocks
                deal_data.append((last_trade_stocks, float(sell_object.price), "Transaction complete",
                                  buy_object.user_id, buy_object.id, buy_object.item_id,
                                  sell_object.user_id, sell_object.id))
                deal_data = []
                break
    return deal_data