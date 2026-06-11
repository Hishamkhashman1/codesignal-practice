#Q2/Q3 — First Non-Repeating Character

#Given a string:

text = "aabbcddee"

#Return:

#"c"

def solution(text):
    seen = []

    for c in text:
        if c not in seen and text.count(c) == 1:
            return c
        else:
            seen.append(c)
    return None

