from collections import deque

HEALING_ITEMS = {
    'Patch': 30,
    'Bandage': 40,
    'MedKit': 100,
}

MAX_RESOURCES = HEALING_ITEMS['MedKit']


def combine_and_create(current_textile, current_medicament):
    combine_elements = current_textile + current_medicament

    for item, value in HEALING_ITEMS.items():
        if combine_elements == value:
            created_items[item] = created_items.get(item, 0) + 1
            return

    if combine_elements > MAX_RESOURCES:
        remaining_resources = combine_elements - MAX_RESOURCES
        created_items['MedKit'] = created_items.get('MedKit', 0) + 1
        if medicaments:
            medicaments[-1] += remaining_resources

    else:
        medicaments.append(current_medicament + 10)


textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

created_items = {}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    combine_and_create(current_textile, current_medicament)

if not textiles and not medicaments:
    print('Textiles and medicaments are both empty.')
elif not textiles:
    print('Textiles are empty.')
else:
    print('Medicaments are empty.')

if created_items:
    sorted_items = sorted(created_items.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    for item_name, amount in sorted_items:
        print(f'{item_name} - {amount}')

if textiles:
    print(f'Textiles left: {", ".join(map(str, textiles))}')

if medicaments:
    print(f'Medicaments left: {", ".join(map(str, reversed(medicaments)))}')