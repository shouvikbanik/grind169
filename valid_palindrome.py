import re


def valid_palindrome(s):
    s = s.lower()
    s = re.sub('[\W_]+', '', s)
    lptr = 0
    rptr = len(s) - 1
    while lptr < rptr:
        if s[lptr] != s[rptr]:
            return False
        lptr += 1
        rptr -= 1
    return True
