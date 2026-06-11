s1 = "aabcc"
s2 = "adcaa"

#return the sum of the minimum number of characters in common between the two strings

# a -> min(2,3) = 2
# b -> min(1,0) = 0
# c -> min(2,1) = 1
# d -> min(0,1) = 0

# Output = 2 + 0 + 1 + 0 = 3

def solution(s1,s2):
    #compare c in s1 and s2 , if it exists in both take min 
    seen = []
    count = 0
    for c in s1:
        if c in s2 and c not in seen:
            count += min(s1.count(c),s2.count(c))
            seen.append(c)


    return count
print (solution(s1,s2))
