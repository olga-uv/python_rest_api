beverages = [
    {"name": "Cola", "price": "100"},
    {"name": "Pepsi", "price": "120"},
    {"name": "Лимонад Колокольчик", "price": "49"},
    {"name": "Минеральная вода", "price": "60"}
    ]

dict_to_checking = {"pocket_1": "wallet", "pocked_2": "keys",
                    "bag": "knife", "backpack": "alcohol",
                    "suitcase": "rarity"}

prohibited_items_dict = {"weapon": ("gun", "knife", "grenade"),
                         "prohibited_substances": ("alcohol", "prescription drugs", "drugs"),
                         "other": ("rarity",)}


def count_by_prohibited_items_and_category(check_dict, prohibited_items):
    count_by_prohibited = 0
    prohibited_category = []
    for items_list in prohibited_items:
        items_in_prohibited_list = prohibited_items[items_list]
        for items in items_in_prohibited_list:
            for places in check_dict:
                if items in check_dict[places]:
                    count_by_prohibited += 1
    return count_by_prohibited


def get_cheapest_goods(goods_list, price):
    cheapest_goods_list = []
    for goods in goods_list:
        if price > int(goods['price']):
            cheapest_goods_list.append(goods["name"])
    return cheapest_goods_list


#print(get_cheapest_goods(beverages, 101))
print(count_by_prohibited_items_and_category(dict_to_checking, prohibited_items_dict))
