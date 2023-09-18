text = tuple(input())

text_set = set(text)

for character in sorted(text_set):
    print(f"{character}: {text.count(character)} time/s")
