text = "abcde"
print(list(text))

# return true if every charec appears once, return false if any char appears more than once
# count = 0
# dup_list = []
#
# for letter in list(text):
#     if letter in dup_list:
#         print (False)
#     else:
#         dup_list.append(letter)
#         print (True)
#
# print(dup_list)
#
# def solution(text):
#     for letter in list(text):
#         dup_list = []
#         if letter in dup_list:
#             return False
#         else:
#             dup_list.append(letter)
#             return True
# print (solution(text))

def solution_2(text):
    dup_list = []
    for letter in list(text):
        if letter in dup_list:
            return False
        else:
            dup_list.append(letter)
    return True
print (solution_2(text))

