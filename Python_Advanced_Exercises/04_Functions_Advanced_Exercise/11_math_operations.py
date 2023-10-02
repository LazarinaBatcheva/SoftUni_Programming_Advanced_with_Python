def math_operations(*args, **kwargs):
    num_pos = 1
    result = ""
    for number in args:
        if num_pos == 1:
            kwargs["a"] += number
        elif num_pos == 2:
            kwargs["s"] -= number
        elif num_pos == 3:
            if number > 0:
                kwargs["d"] /= number
        elif num_pos == 4:
            kwargs["m"] *= number
        num_pos += 1
        if num_pos > 4:
            num_pos = 1
    for key, value in sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0])):
        result += f"{key}: {value:.1f}\n"
    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print()
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print()
print(math_operations(6.0, a=0, s=0, d=5, m=0))
