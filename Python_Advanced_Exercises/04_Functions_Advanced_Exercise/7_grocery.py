def grocery_store(**kwargs):
    receipt = dict(sorted(kwargs.items(), key=lambda kvp: (-(kvp[1]), -len(kvp[0]), kvp[0])))
    result = []
    for product, quantity in receipt.items():
        result.append(f"{product}: {quantity}")
    return "\n".join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print()
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
