from collections import deque

quantity_of_food = int(input())
food_for_each_order = deque([int(number) for number in input().split()])

print(max(food_for_each_order))

while food_for_each_order:
    first_element = food_for_each_order[0]
    if first_element <= quantity_of_food:
        food_for_each_order.popleft()
        quantity_of_food -= first_element
    else:
        break

if food_for_each_order:
    print("Orders left: ", end="")
    while food_for_each_order:
        print(food_for_each_order.popleft(), end=" ")
else:
    print("Orders complete")
