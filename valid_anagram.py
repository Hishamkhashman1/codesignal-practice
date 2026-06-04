# Valid anagram excercise

# assume two strings s1 and s2

s1 = "evil"
s2 = "vile"

# TODO : validate if two strings are anagrams (meaning have the same letters with the same frequencies)

def validate_anagrams(s1,s2):
    #TODO: validate that they first have the same letters
    if list(s1).sort() == list(s2).sort():
        return True
    return False
print (validate_anagrams(s1,s2))
