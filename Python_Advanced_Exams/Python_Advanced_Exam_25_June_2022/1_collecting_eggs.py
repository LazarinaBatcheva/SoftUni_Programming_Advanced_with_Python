from collections import deque

BOX_SIZE = 50
BAD_LUCK_EGG = 13

eggs_sizes = deque(int(x) for x in input().split(', '))
paper_pieces = [int(x) for x in input().split(', ')]

filled_box_count = 0

while eggs_sizes and paper_pieces:
    current_egg = eggs_sizes.popleft()

    if current_egg <= 0:
        continue

    elif current_egg == BAD_LUCK_EGG:
        paper_pieces[0], paper_pieces[-1] = paper_pieces[-1], paper_pieces[0]
        continue

    current_paper = paper_pieces.pop()
    egg_paper_sum = current_egg + current_paper

    if egg_paper_sum <= BOX_SIZE:
        filled_box_count += 1

if filled_box_count:
    print(f'Great! You filled {filled_box_count} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_sizes:
    print(f'Eggs left: {", ".join(map(str, eggs_sizes))}')

if paper_pieces:
    print(f'Pieces of paper left: {", ".join(map(str, paper_pieces))}')