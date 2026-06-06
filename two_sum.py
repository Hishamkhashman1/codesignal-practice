# two sum problem

# from an array need to add two numbers to get a target

#bruteforce, inception loops
nums = [2,7,11,15]
target = 13

def two_sum(nums, target):
    n = len(nums)
    for i in range (n):
        for j in range (i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]
    return None

print (two_sum(nums, target))

#hashmap

def two_sum_hashmap(nums, target):
    hashmap = {}
    for i, num in enumerate (nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff],i]
        hashmap[num] = i
    return None

print (two_sum_hashmap(nums, target))

