def sum_nums(num1, num2):
    result = num1 + num2
    return f'{result:.2f}'


def subtract_nums(num1, num2):
    result = num1 - num2
    return f'{result:.2f}'


def multiply_nums(num1, num2):
    result = num1 * num2
    return f'{result:.2f}'


def divide_nums(num1, num2):
    try:
        result = num1 / num2
        return f'{result:.2f}'
    except ZeroDivisionError:
        return None


def power_nums(num1, num2):
    result = num1 ** num2
    return f'{result:.2f}'
