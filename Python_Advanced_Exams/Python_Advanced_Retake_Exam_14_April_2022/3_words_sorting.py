def words_sorting(*words):
    words_dict = {}
    total_sum = 0

    for word in words:
        words_dict[word] = sum(ord(letter) for letter in word)
        total_sum += words_dict[word]

    if total_sum % 2 == 0:
        sorted_dict = sorted(words_dict.items(), key=lambda kvp: kvp[0])
    else:
        sorted_dict = sorted(words_dict.items(), key=lambda kvp: -kvp[1])

    return '\n'.join(f'{current_word} - {current_sum}' for current_word, current_sum in sorted_dict)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print()
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print()
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
