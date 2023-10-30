from pyfiglet import figlet_format


def print_art(text_):
    ascii_art = figlet_format(text)
    print(ascii_art)


text = input()

print_art(text)