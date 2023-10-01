def numbers_sums(*args):
    negatives_sum = 0
    positives_sum = 0

    for number in args:
        if number > 0:
            positives_sum += number
        else:
            negatives_sum += number

    return negatives_sum, positives_sum


some_numbers = [int(x) for x in input().split()]

print(numbers_sums(*some_numbers)[0])
print(numbers_sums(*some_numbers)[1])

if abs(numbers_sums(*some_numbers)[0]) > numbers_sums(*some_numbers)[1]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
