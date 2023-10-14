from collections import deque


tools = deque(int(x) for x in input().split())
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

is_success = False

while tools and substances:
    current_tool = tools[0]
    current_substance = substances[-1]
    result = current_tool * current_substance

    if challenges:
        if result in challenges:
            challenges.remove(result)
            tools.popleft()
            substances.pop()
        else:
            tools[0] += 1
            tools.rotate(-1)
            if (substances[-1] - 1) == 0:
                substances.pop()
            else:
                substances[-1] -= 1

    if not challenges:
        is_success = True
        print('Harry found an ostracon, which is dated to the 6th century BCE.')
        break

if not is_success:
    print('Harry is lost in the temple. Oblivion awaits him.')

if tools:
    print(f'Tools: {", ".join(map(str, tools))}')
if substances:
    print(f'Substances: {", ".join(map(str, substances))}')
if challenges:
    print(f'Challenges: {", ".join(map(str, challenges))}')