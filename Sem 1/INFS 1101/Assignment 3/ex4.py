def PathFinder(s):
    safecount = 0
    maxcount = 0
    i = 0
    while i < len(s):
        if s[i] == 'S':
            safecount += 1
            if maxcount < safecount:
                maxcount = safecount
        else:
            safecount = 0
        i += 1
    return maxcount

path = input("Enter the path: ")
print(f"Longest safe sequence: {PathFinder(path)}")