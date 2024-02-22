# Gowshikrajan
# 60307390
# INFS1101 - 16
# TemperatureContemplator

temp_c = float(input("Enter predicted temperature in Celsius: "))

temp_f = (9/5)*temp_c + 32

print(f"The temperature in Fahrenheit is {temp_f}⁰F.")

if 70 <= temp_f <= 80:
    print("Perfect weather for an outdoor picnic!")
elif temp_f > 80:
    print("It might be too hot for an outdoor picnic.")
else:
    print("Might be too cold for an outdoor picnic.")

