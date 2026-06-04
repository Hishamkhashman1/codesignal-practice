s = "abbffdd"
chars =list(s)

#find and return the first character that appears exactly once in the string. If there is no such character, return "_"
def string_dup(chars):
    for c in chars:
        if chars.count(c) == 1:
            return c
    return "_"

print(string_dup(chars))

