def age_assignment(*args, **kwargs):
    persons_info = {}
    for name in args:
        persons_info[name] = kwargs[name[0]]
    sorted_persons = sorted(persons_info.items(), key=lambda kvp: kvp[0])
    result = []
    for name, age in sorted_persons:
        result.append(f"{name} is {age} years old.")
    return "\n".join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print()
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
