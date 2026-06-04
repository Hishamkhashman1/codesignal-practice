# almost increasing sequence

# Given an array of integers, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element.

# A sequence is strictly increasing if a[i] < a[i+1]

# examples [1,3,2,1] --> False, [1,3,2] --> TRUE, [1,2,3,4] --> TRUE, [1,2,1,2] --> FALSE, [10,1,2,3,4] --> True

a = [1,2,3,2,3]
b = []

#print (n)

def almost_increasing_seq(a):
    for i in range (len(a)):
        test = a[:i] + a[i+1:]   # slices the array before i and after i, creating a new array called test which doesnt have i

        is_increasing = True

        for h in range (len(test)-1):
            if test[h] >= test[h+1]:
                is_increasing = False
                break
        if is_increasing:
            return True
    return False
print (almost_increasing_seq(a))
