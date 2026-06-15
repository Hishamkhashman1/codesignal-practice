# 345. Reverse Vowels of a String
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
#
#
# Example 1:
#
# Input: s = "IceCreAm"
#
# Output: "AceCreIm"
#
# Explanation:
#
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
#
# Example 2:
#
# Input: s = "leetcode"
#
# Output: "leotcede"
#
#
#
# Constraints:
#
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

s = "IceCream"

def solution (s):
    vowels = "aeiou"
    result_not_vowel = []
    result_vowel = []
    s = list(s)
    output_tupple = []

# loop through charecters in s, if charecter is not vowel keep same index and append to result, if charecter is vowel append to result with index[::-1]

    for i in range (len(s)):
        if s[i].lower() not in vowels:
            result_not_vowel.append((s[i],i))
        if s[i].lower() in vowels:
            result_vowel.append((s[i],i))
    print (result_not_vowel)
    print (result_vowel)

    vowels_letters = []

    for rv in result_vowel:
        vowels_letters.append(rv[0])

    result_vowels_reversed = []

    for i in range (len(vowels_letters)):
        current_index = result_vowel[i][1]

        rev_index = len(vowels_letters) - 1 - i

        reversed_vowel = vowels_letters[rev_index]

        result_vowels_reversed.append((reversed_vowel,current_index))

    output_tupple = result_not_vowel + result_vowels_reversed
    output_list = [None]* (len(s))

    for element in output_tupple:
        c = element[0]
        i = element[1]
        output_list[i] = c


    print (output_tupple)
    print (output_list)

    return ("".join(output_list))


print (solution(s))

