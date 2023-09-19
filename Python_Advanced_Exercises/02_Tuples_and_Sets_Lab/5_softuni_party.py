guests = set(input() for code in range(int(input())))
came_guest = input()

while came_guest != "END":
    if came_guest in guests:
        guests.remove(came_guest)
    came_guest = input()

print(len(guests))

for guest in sorted(guests):
    print(guest)