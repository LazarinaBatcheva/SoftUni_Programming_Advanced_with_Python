def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    if word[index] != word[-1 - index]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)


print(palindrome("abcba", 0))
print()
print(palindrome("peter", 0))
