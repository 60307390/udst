def CelestialDecoder(s):
    i = 0
    strs = 0
    plnts = 0
    while i < len(s):
        if i % 2 == 0:
            strs += int(s[i])
        else:
            plnts += int(s[i])
        i += 1
    return strs, plnts


code = input("Enter the constellation code string: ")

while not code.isdigit():
    print("Invalid input")
    code = input("Enter the constellation code string: ")

stars, planets = CelestialDecoder(code)
print(f"Total Stars: {stars}, Total Planets: {planets}")