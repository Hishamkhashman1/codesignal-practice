# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

l1 = [2,4,3]
l2 = [5,6,4]

l1_rev = l1[::-1]
l2_rev = l2[::-1]

print ("".join(map(str,l1_rev)))
#use int(str) to convert to int

def add_two_nums(l1,l2):
    l1_int_reverse = int("".join(map(str,l1[::-1])))
    l2_int_reverse = int("".join(map(str,l2[::-1])))
    sum = l1_int_reverse + l2_int_reverse

    reversed_sum = int(str(sum)[::-1])

    result = list(map(int, str(reversed_sum)))
    return result


print( add_two_nums(l1,l2))


