def shopping_cart(*products):
    meals_limit = {'Soup': 3, 'Pizza': 4, 'Dessert': 2}
    meals = {'Soup': [], 'Pizza': [], 'Dessert': []}
    for element in products:
        if element == 'Stop':
            break
        meal, product = element
        if meal in meals.keys() and product not in meals[meal] and len(meals[meal]) != meals_limit[meal]:
            meals[meal].append(product)

    result = ''

    if all(not meals[meal] for meal in meals.keys()):
        result += 'No products in the cart!'
    else:
        sorted_meals = sorted(meals.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
        for meal_type, added_product in sorted_meals:
            result += f'{meal_type}:\n'
            for current_product in sorted(added_product):
                result += f' - {current_product}\n'

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print()
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print()
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
