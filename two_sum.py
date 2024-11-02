def two_sum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        if target - nums[i] in hashmap:
            return i, hashmap[target - nums[i]]
        else:
            hashmap[nums[i]] = i
