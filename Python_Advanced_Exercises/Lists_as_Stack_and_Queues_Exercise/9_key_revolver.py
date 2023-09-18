from collections import deque

price_for_a_bullet = int(input())
gun_barrel_size = int(input())
bullets = list(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
intelligences_value = int(input())

shots_counter = 0

while locks:
    if bullets:
        current_bullet = bullets.pop()
        if current_bullet <= locks[0]:
            print("Bang!")
            locks.popleft()
        else:
            print("Ping!")

        shots_counter += 1
        intelligences_value -= price_for_a_bullet

        if shots_counter == gun_barrel_size and bullets:
            print("Reloading!")
            shots_counter = 0
    else:
        break

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligences_value}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")