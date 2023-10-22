from collections import deque

vowels = deque(letter for letter in input().split())
consonants = [letter for letter in input().split()]

words = {
    'rose': set('rose'),
    'tulip': set('tulip'),
    'lotus': set('lotus'),
    'daffodil': set('daffodil'),
}

found_letters = {
    'rose': set(),
    'tulip': set(),
    'lotus': set(),
    'daffodil': set(),
}

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    word_found = False

    for word, letters in words.items():
        if current_vowel in letters:
            found_letters[word].add(current_vowel)

        if current_consonant in letters:
            found_letters[word].add(current_consonant)

        if letters == found_letters[word]:
            print(f'Word found: {word}')
            word_found = True
            break

    if word_found:
        break

else:
    print('Cannot find any word!')

if vowels:
    print(f'Vowels left: {" ".join(vowels)}')

if consonants:
    print(f'Consonants left: {" ".join(consonants)}')