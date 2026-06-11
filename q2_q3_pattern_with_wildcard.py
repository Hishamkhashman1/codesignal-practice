# Q2/Q3 — Pattern With Wildcard
#
# You are given two strings:
#
# pattern
# source
#
# pattern contains only:
#
# 0, 1, ?
#
# source contains only lowercase English letters.
#
# Rules:
#
# 0 = vowel
# 1 = consonant
# ? = either vowel or consonant
#
# Return the number of substrings of source that match pattern.
#
# Vowels are:
#
# "a", "e", "i", "o", "u", "y"
# Example 1
pattern = "0?0"
source = "amazing"
#
def solution(pattern, source):
    vowels = "aeiouy"
    source_bin = ""
    count = 0
    
    for c in source:
        if c in vowels:
            source_bin += "0"
        else:
            source_bin += "1"

    pattern_len = len(pattern)

    for i in range(len(source_bin) - pattern_len + 1):
        current_slice = source_bin[i : i + pattern_len]
        match = True

        for j in range(len(pattern)):
            if pattern[j] != "?" and pattern[j] != current_slice[j]:
                match = False
        if match:
            count += 1

    return count
print (solution(pattern, source))

