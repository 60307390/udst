##
# Gowshikrajan Senthilkumar - 60307390
# Week11 lab
# Exercise 1

def view_menu():
    max_length = 0
    N = 2       # For Tab Length
    for i in menuDict.keys():
        if len(i) > max_length:
            max_length = len(i)
    
    for i, j in menuDict.items():
        print(f"{i}{str(j).rjust(max_length+(4*N)-len(i))}")

def add_item(item, price):
    menuDict[item] = price

def update_item(item, price):
    menuDict.update({item:price})

def delete_item(item):
    menuDict.pop(item)


menuDict={'soup':12, 'salad':15,
           'hummus':10, 'fattoush':13, 'tabbouleh':17,
           'musakhan':32, 'maqluba':28, 'mansaf':40,
           'kibbeh':52, 'kebab':45, 'mandi':34, 'biryani':25,
           'pizza':19, 'burger':22, 'fries':12,
           'kunefe':15, 'cheesecacke':23, 'brownie':21}

while True:
    try:
        choice = int(input("************************************************************\nWelcome to restaurant management system\n1: view menu\n2: add new item\n3: update existing item\n4: delete item\n0: exit\nWhich operations do you want to perform (0 to 4)? "))
    except:
        print("Invalid input!")
        choice = -1
    
    if choice == 1:
        view_menu()
        
    if choice == 2:
        item = input("What item would you like to add? ")
        price = int(input("What is the price of karak? "))
        add_item(item, price)
        
    if choice == 3:
        item = input("What item would you like to update? ")
        if item in menuDict:
            price = input("What is the new price of karak? ")
            update_item(item, price)
        else:
            print(f"{item} is not in the menu. If you want to add it, select operation 2")
            
    if choice == 4:
        item = input("What item would you like to remove? ")
        if item in menuDict:
            delete_item(item)
        else:
            print(f"{item} is not in the menu.")
            
    if choice == 0:
        print("Goodbye!")
        break
