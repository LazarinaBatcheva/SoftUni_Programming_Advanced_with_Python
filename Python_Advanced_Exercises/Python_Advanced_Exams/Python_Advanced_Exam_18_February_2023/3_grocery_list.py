from typing import List, Tuple


def shop_from_grocery_list(budget: int, grocery_list: List[str], *products_info: Tuple[str, float]):
    bought_products = {}

    for product, price in products_info:
        if product in grocery_list:
            if price <= budget:
                if product not in bought_products.keys():
                    bought_products[product] = bought_products.get(product, 0) + price
                    budget -= price
                    grocery_list.remove(product)
            else:
                break

    result = ''

    if not grocery_list:
        result += f'Shopping is successful. Remaining budget: {budget:.2f}.'
    else:
        result += f'You did not buy all the products. Missing products: {", ".join(grocery_list)}.'

    return result


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
