#Given an array a, find the first value that appears more than once.

#The first duplicate is the value whose second occurrence has the smallest index.

#If there are no duplicates, return -1

a = [2,1,3,5,3,2]
b = []
# transform array into dictionary with indices
def find_first_duplicate(a):
    for i in a:
        if i in b:
            return i
        b.append(i)

    return -1

print (find_first_duplicate(a))



