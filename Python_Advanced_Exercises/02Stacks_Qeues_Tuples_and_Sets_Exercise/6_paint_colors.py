from collections import deque

colors_string = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"],
}
found_colors = []

while colors_string:
    first_substring = colors_string.popleft()
    last_substring = colors_string.pop() if colors_string else ""

    if first_substring + last_substring in main_colors or first_substring + last_substring in secondary_colors:
        found_colors.append(first_substring + last_substring)

    elif last_substring + first_substring in main_colors or last_substring + first_substring in secondary_colors:
        found_colors.append(last_substring + first_substring)

    else:
        if len(first_substring) > 1:
            colors_string.insert(len(colors_string) // 2, first_substring[:-1])

        if len(last_substring) > 1:
            colors_string.insert(len(colors_string) // 2, last_substring[:-1])

for color in found_colors:
    if color in secondary_colors:
        for element in secondary_colors[color]:
            if element not in found_colors:
                found_colors.remove(color)

print(found_colors)