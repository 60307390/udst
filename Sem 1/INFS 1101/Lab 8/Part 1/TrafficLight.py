# Gowshikrajan
# 60307390
# INFS 1101 - 16
# TrafficLight

light = input("What is the color of the traffic light (green/red/yellow)? ")
light = light.lower()

if light == 'green':
    print("Keep going!")
elif light == 'yellow':
    print("Slow down!")
elif light == 'red':
    print("Stop the car!")
else:
    print("This is not a valid entry.")
