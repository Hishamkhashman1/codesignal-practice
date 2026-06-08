# Question 3 - You are given an array of integers (numbers)

# your task is to determine whether any value appears more than once in the array

# return True if at least one duplciate exists else return False

numbers = [1,2,3,2]

def solution(numbers):
    test = []
    for n in numbers:
        if n in test:
            return True
        else:
            test.append(n)
    return False
print (solution(numbers))
