# Gowshikrajan
# 60307390
# INFS 1101 - 16
# RicePriceOptimizing

w1 = float(input("Enter weight of package 1: "))
p1 = float(input("Enter price of package 1: "))
w2 = float(input("Enter weight of package 2: "))
p2 = float(input("Enter price of package 2: "))

#The ratio of weight to price, i.e, value
r1 = w1 / p1
r2 = w2 / p2

if r1 > r2: #If value of package 1 > value of package 2
    print("Package 1 the better price.")
else:
    print("Package 2 the better price.")
