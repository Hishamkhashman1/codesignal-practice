string = "amaing"

# which character appears 2 times and any of its neigbours is a vowel

def solution(string):
    vowels = list("aeiouy")
    seen = []

    for i in range(len(string)):
        if string[i] in seen:
            if string[i - 1] in vowels or string[i + 1] in vowels:
                return string[i]
        else:
            seen.append(string[i])
print (solution(string))



