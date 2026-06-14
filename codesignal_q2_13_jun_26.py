codelength = 55

breakpoints = [2,5,16,44]

actions = ["next", "next", "continue", "next","next"]

# output is 7 because next adds 1 and then continue goes to second breakpoint then we add another two

def solution(codelength, breakpoints, actions):
    line = 1

    breakpoints = sorted(breakpoints)

    for a in actions:
        if a == "next":
            if line < codelength:
                line += 1

        elif a == "continue":
            for bp in breakpoints:
                if bp > line:
                    line = bp
                    break
            else:
                line = codelength
    return line
print (solution( codelength, breakpoints, actions))
