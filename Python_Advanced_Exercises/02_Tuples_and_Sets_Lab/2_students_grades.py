number_of_lines = int(input())

students_info = {}

for _ in range(number_of_lines):
    name, grade = tuple(input().split())
    if name not in students_info.keys():
        students_info[name] = []
    students_info[name].append(float(grade))

for student, grades in students_info.items():
    formatted_grades = " ".join([f'{current_grade:.2f}'for current_grade in grades])
    print(f"{student} -> {formatted_grades} (avg: {sum(grades) / len(grades):.2f})")