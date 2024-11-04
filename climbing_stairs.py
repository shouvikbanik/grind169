"""
Naive with TLE
def climbing_stairs(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbing_stairs(n - 1) + climbing_stairs(n - 2)
"""
hashmap = {}


def climbing_stairs(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n in hashmap:
        return hashmap[n]
    else:
        return_val = climbing_stairs(n - 1) + climbing_stairs(n - 2)
        hashmap[n] = return_val
        return return_val
