class CheckVersion(object):
    def __init__(self):
        self.count = 0

    def is_bad_version(self, n):
        self.count += 1
        if n == 4:
            return True
        else:
            return False


def first_bad_version(obj, n):
    l, r = 1, n
    last_positive = -1
    while l <= r:
        mid = (l + r) // 2
        if obj.is_bad_version(mid):
            r = mid - 1
            last_positive = mid
        else:
            l = mid + 1
    return last_positive
