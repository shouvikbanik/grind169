def longest_palindrome(s):
    length = 0
    odd = set()
    for char in s:
        if char in odd:
            length += 2
            odd.remove(char)
        else:
            odd.add(char)
    if len(odd) >= 1:
        return length + 1
    else:
        return length
