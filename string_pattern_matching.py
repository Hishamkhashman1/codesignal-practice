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

vowels = ["a", "i", "e", "o", "u", "y"]

arr_source = list(source)

print (arr_source)

for item in arr_source:
    if item in vowels:
        print ("0")
    else:
        print ("1")
# convert string source to array



#loop through items in array and check them against vowels, if match change them to 0 , if anything else 1

# slice 3 items and loop through 3 items to match pattern, if match count += 1

# return count
