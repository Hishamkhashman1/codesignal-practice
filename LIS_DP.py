# nums = [3,1,8,2,5]
#output of LIS will be = 3 .. becasue 1 then 2 then 5 

nums = [5,2,8,6,3,6,9,5]
#output of LIS will be = 4 .. becasue 2 then 3 then 6 then 9

def lis(nums):
    L = [1] * len(nums) # L[i] is the length of the longest increasing subsequence ending at index i

    for i in range (1, len(L)):
        subsets = []
        for j in range (0,i):
            if nums[j] < nums[i]:
                subsets.append(L[j])
            else:
                continue

        L[i] = 1 + max(subsets, default=0)


    return max(L, default=0)

print (lis(nums))
