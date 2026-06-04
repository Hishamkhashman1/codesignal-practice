s = "racecar"


def palindrom_check(s):
    lc = list(s)

    print (lc)

    reversed_lc = lc[::-1]

    print (reversed_lc)

    s_reversed = "".join(reversed_lc)

    print (s_reversed)

    if s == s_reversed:
        return True
    return False

print(palindrom_check(s))
