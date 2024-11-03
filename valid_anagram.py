def is_anagram(s, t):
    hashmap = {}
    for char in s:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1
    for char in t:
        if char in hashmap and hashmap[char] > 0:
            hashmap[char] -= 1
            if hashmap[char] == 0:
                hashmap.pop(char)
        else:
            return False
    if not hashmap:
        return True
    else:
        return False
