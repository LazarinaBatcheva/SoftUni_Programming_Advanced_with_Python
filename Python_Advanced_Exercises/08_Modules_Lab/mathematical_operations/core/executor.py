from core.operations import sum_nums, subtract_nums, multiply_nums, divide_nums, power_nums

sign_mapper = {
    '+': sum_nums,
    '-': subtract_nums,
    '*': multiply_nums,
    '/': divide_nums,
    '^': power_nums,
}


def execute_string(math_string):
    num1, sign, num2 = math_string.split()
    num1, num2 = float(num1), int(num2)
    return sign_mapper[sign](num1, num2)
