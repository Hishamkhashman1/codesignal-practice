s = "banana"

def count_letters(s):
    s_list = list(s)
    count = {}
    for letter in s_list:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count


print (count_letters(s))
