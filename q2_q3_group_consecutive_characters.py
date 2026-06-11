# given a string 
text = "aaabbccccd"

# Return:
#
# [
#     ("a", 3),
#     ("b", 2),
#     ("c", 4),
#     ("d", 1)
# ]
#
# because:
#
# aaa -> 3
# bb -> 2
# cccc -> 4
# d -> 1
def solution(text):
    current_char = text[0]
    result = []
    current_count = 1

    for i in range(1, len(text)):
        if text[i] == current_char:
            current_count +=1
        else:
            result.append((current_char, current_count))

            current_char = text[i]
            current_count = 1

    result.append((current_char, current_count))

    return result

print (solution(text))
