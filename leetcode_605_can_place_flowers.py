# 605. Can Place Flowers
# Easy
# Topics
# premium lock icon
# Companies
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
#
#
#
# Example 1:
#
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:
#
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#
#
# Constraints:
#
# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

flowerbed = [0]
n = 1


# def solution(flowerbed, n):
#     can_plant = []
#
#     for i in range (len(flowerbed)-1):
#         if flowerbed[i+1] == 0 :
#             can_plant.append(True)
#     if can_plant.count(True) - n == 2:
#         return True
#     else:
#         return False
# print (solution(flowerbed, n))


# def solution(flowerbed, n):
#     possible_plant = []
#
#     for i in range (len(flowerbed)):
#         if flowerbed[0] == 1:
#             if flowerbed[i] == 0:
#                     if flowerbed[i+1] == 0:
#                         if flowerbed[i+2] == 0:
#                             flowerbed[i+1] = 1
#                             possible_plant.append(flowerbed[i+1])
#     if possible_plant.count(1) >= n:
#         return True
#     else: 
#         return False
# print (solution(flowerbed, n))

def solution(flowerbed, n):
    can_plant = []

    for i,f in enumerate(flowerbed):
        if f == 1:
            can_plant.append("Nop")
        else:
            if f == 0:
                can_plant.append("maybe")

    if len(can_plant) > 1:

        for i in range (len(can_plant)):

            if can_plant[i] == "maybe" and can_plant[i-1] == "maybe" and can_plant[i+1] == "maybe":
                can_plant[i] = "ahuevo"
            if can_plant[0] == "maybe" and can_plant[1] == "maybe":
                can_plant[0] = "ahuevo"
            if can_plant[-1] == "maybe" and can_plant[-2] == "maybe":
                can_plant[-1] = "ahuevo"
    else:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            can_plant[0] = "ahuevo"

    print (n)
    print(can_plant)
    print(can_plant.count("ahuevo"))
    if can_plant.count("ahuevo") >= n:
        return True
    else:
        return False

print (solution(flowerbed, n))

