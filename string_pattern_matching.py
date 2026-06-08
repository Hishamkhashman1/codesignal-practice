# You are given two strings, pattern and source.

# The string pattern contains only the characters '0' and '1'.

# The string source contains only lowercase English letters.

# Your task is to calculate the number of substrings of source that match pattern.

# the substring and pattern have the same length.

# pattern 0 is for a vowel. lets assume vowels are a, i, e ,o, u, y

# pattern 1 is for consonants (i.e. every thing else)

# eample for pattern = "010" and source = "amazing" , out put would be 2. ama = 010  and azi = 010

pattern = "010"

source = "amazing"


def string_pattern_matching(pattern, source):
    vowels = ["a", "i", "e", "o", "u", "y"]
    count = 0
    source_transformed = []
    arr_source = list(source)

    for item in arr_source:
        if item in vowels:
            source_transformed.append("0")

        else:
            source_transformed.append("1")

    for i in range (len(source_transformed)-len(pattern)+1):
        test = "".join(source_transformed[i:i+ len(pattern)])
        if test == pattern:
            count += 1
    return (count)
