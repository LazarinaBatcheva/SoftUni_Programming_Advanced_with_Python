def gather_credits(max_credits: int, *args: (str, int)):
    courses = []
    gathered_credits = 0
    result = ''

    for course, course_credits in args:
        if course not in courses:
            if gathered_credits < max_credits:
                courses.append(course)
                gathered_credits += course_credits
            else:
                break

    if gathered_credits >= max_credits:
        result += f'Enrollment finished! Maximum credits: {gathered_credits}.\n'
        result += f'Courses: {", ".join(sorted(courses))}'
    else:
        credits_shortage = max_credits - gathered_credits
        result += f'You need to enroll in more courses! You have to gather {credits_shortage} credits more.'

    return result


print(gather_credits(
    80,
    ("Basics", 27),
))
print()
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print()
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))


