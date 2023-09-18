number_of_lines = int(input())

longest_intersection = set()

for _ in range(number_of_lines):
    start_end_numbers = input().split("-")
    f_start, f_end = (int(x) for x in start_end_numbers[0].split(","))
    s_start, s_end = (int(x) for x in start_end_numbers[1].split(","))

    left_range = set(range(f_start, f_end + 1))
    right_range = set(range(s_start, s_end + 1))

    repeat_nums = left_range & right_range

    if len(repeat_nums) > len(longest_intersection):
        longest_intersection = repeat_nums

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")