# First Missing Positive Integer
#
# Given a list of integers:
#
# numbers
#
# Return the smallest positive integer that does not appear in the list.
#
# Example 1
numbers =[-5, -2, 0, 1, 2]
#
# Output:
#
# 4
#
# because:
#
# 1 exists
# 2 exists
# 3 exists
# 4 is missing
def solution(numbers):
    sorted_numbers = sorted(numbers)
    integer = []
    pos_integer = []
    integer.append(sorted_numbers[len(sorted_numbers)-1]+1)  
    for i in range(len(sorted_numbers)-1):
        
        if sorted_numbers[i] > 0:
         
            if i == 0 and sorted_numbers[i] != 1:
                integer.append(1)

            else:
                if sorted_numbers[i] + 1 != sorted_numbers[i+1]:
                    integer.append(sorted_numbers[i]+1)
    
    for n in integer:
        if n > 0:
            pos_integer.append(n)

    return min(pos_integer)
