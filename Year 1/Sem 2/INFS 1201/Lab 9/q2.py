##
# Gowshikrajan Senthilkumar - 60307390
# Week11 lab
# Exercise 2

menuDict={'soup':12, 'salad':15,
           'hummus':10, 'fattoush':13, 'tabbouleh':17,
           'musakhan':32, 'maqluba':28, 'mansaf':40,
           'kibbeh':52, 'kebab':45, 'mandi':34, 'biryani':25,
           'pizza':19, 'burger':22, 'fries':12,
           'kunefe':15, 'cheesecacke':23, 'brownie':21}

orderDict = {}

while True:
    item = input("What would you like to order? ")

    if item == 'exit':
        break
    if item not in menuDict:
        print(f"We do not sell {item}. Please choose something else.")
    else:
        quantity = int(input(f"How much {item} would you like to order? " ))
        orderDict[item] = quantity

total_bill = 0
print("Here is a summary of your order: ")
for k, v in orderDict.items():
    print(f"- {k} : {v}")
    total_bill += menuDict[k]*v

print(f"Total bill: {total_bill}QAR.")


