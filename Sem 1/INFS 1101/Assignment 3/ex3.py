def FuelManager(f_i, p):
    i = 0
    deltaF = 0
    x, y = 0, 0
    while i < len(p):
        if p[i] == 'R': 
            x += 1
            deltaF -= 1
        elif p[i] == 'L': 
            x -= 1
        elif p[i] == 'U':
            y += 1
            deltaF -= 1
        elif p[i] == 'D':
            y -= 1
        i += 1
    f = f_i + deltaF
    return x, y, f

fuel = int(input("Enter the initial fuel level: "))
path = input("Enter the journey path: ")

r_x, r_y, remainingFuel = FuelManager(fuel, path)
print(f"Final fuel level: {remainingFuel}, Final position: ({r_x}, {r_y})")