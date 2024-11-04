def ransom_note(ransom_note, magazine):
    dictionary = {}
    for char in magazine:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    for char in ransom_note:
        if char in dictionary:
            dictionary[char] -= 1
            if dictionary[char] == 0:
                dictionary.pop(char)
        else:
            return False
    return True
