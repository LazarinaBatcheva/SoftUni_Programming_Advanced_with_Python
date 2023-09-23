from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

made_presents = {}

while materials and magic:
    total_magic_level = materials[-1] * magic[0]

    if total_magic_level in presents.keys():
        new_present = presents[total_magic_level]
        if new_present not in made_presents.keys():
            made_presents[new_present] = 0
        made_presents[new_present] += 1
        materials.pop()
        magic.popleft()

    elif total_magic_level < 0:
        materials.append(materials.pop() + magic.popleft())

    elif total_magic_level > 0:
        magic.popleft()
        materials[-1] += 15

    elif materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()

    elif materials[-1] == 0:
        materials.pop()

    elif magic[0] == 0:
        magic.popleft()

if (("Doll" in made_presents.keys() and "Wooden train" in made_presents.keys()) or
        ("Teddy bear" in made_presents.keys() and "Bicycle" in made_presents.keys())):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for name, amount in sorted(made_presents.items()):
    print(f"{name}: {amount}")