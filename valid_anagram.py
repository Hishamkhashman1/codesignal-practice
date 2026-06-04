# Valid anagram excercise

# assume two strings s1 and s2

s1 = "hello"
s2 = "world"

# TODO : validate if two strings are anagrams (meaning have the same letters with the same frequencies)

def validate_anagrams(s1,s2):
    #TODO: validate that they first have the same letters
    if sorted(s1) == sorted(s2):
        return True
    return False
print (validate_anagrams(s1,s2))
