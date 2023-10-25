def start_spring(**kwargs):
    objects = {}
    for name, object_type in kwargs.items():
        if object_type not in objects.keys():
            objects[object_type] = []
        objects[object_type].append(name)

    result = ''

    sorted_objects = sorted(objects.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for object_t, object_names in sorted_objects:
        result += f'{object_t}:\n'
        for object_name in sorted(object_names):
            result += f'-{object_name}\n'

    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
print()
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
print()
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
