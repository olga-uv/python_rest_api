beverages = [
    {"name": "Cola", "price": "100"},
    {"name": "Pepsi", "price": "120"},
    {"name": "Лимонад Колокольчик", "price": "49"},
    {"name": "Минеральная вода", "price": "60"}
    ]

dict_to_checking = {"pocket_1": "wallet", "pocked_2": "keys",
                    "bag": "knife", "backpack": "gun",
                    "suitcase": "rarity"}

prohibited_items_dict = {"weapon": ("gun", "knife", "grenade"),
                         "prohibited_substances": ("alcohol", "prescription drugs", "drugs"),
                         "other": ("rarity",)}


emails = {'mgu.edu': ['andrei_serov', 'aleksandr_pushkin', 'elena_belova', 'kirill_stepanov'],
          'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abramova'],
          'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
          'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
          'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
          'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}


def emails_by_abc(emails_list):
    full_emails = []
    for domains in emails_list:
        for emails_in_list in emails_list[domains]:
            full_emails.append(emails_in_list.replace(emails_in_list, emails_in_list + "@" + domains))
    return sorted(full_emails)


def count_by_prohibited_items_and_category(check_dict, prohibited_items):
    count_by_prohibited = 0
    prohibited_category = set()
    for items_list in prohibited_items:
        items_in_prohibited_list = prohibited_items[items_list]
        for items in items_in_prohibited_list:
            for places in check_dict:
                if items in check_dict[places]:
                    count_by_prohibited += 1
                    prohibited_category.add(items_list)
    return count_by_prohibited, prohibited_category


def get_cheapest_goods(goods_list, price):
    cheapest_goods_list = []
    for goods in goods_list:
        if price > int(goods['price']):
            cheapest_goods_list.append(goods["name"])
    return cheapest_goods_list


#print(emails_by_abc(emails))
#print(get_cheapest_goods(beverages, 101))
#print(count_by_prohibited_items_and_category(dict_to_checking, prohibited_items_dict))


a = ["a1", "a2", "a3", "a1"]
a = list(set(a))
print(a)
