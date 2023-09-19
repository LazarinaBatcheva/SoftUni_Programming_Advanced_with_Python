number_of_lines = int(input())

cars_in_parking = set()

for _ in range(number_of_lines):
    direction, car_number = input().split(", ")

    if direction == "IN":
        cars_in_parking.add(car_number)
    else:
        if car_number in cars_in_parking:
            cars_in_parking.remove(car_number)

if cars_in_parking:
    for car in cars_in_parking:
        print(car)
else:
    print("Parking Lot is Empty")