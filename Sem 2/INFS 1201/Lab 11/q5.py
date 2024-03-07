##
# Gowshikrajan Senthilkumar - 60307390
# Week11 lab
# Exercise 5

def maxMenu(menu):
    'returns the dish with the higest price within a given menu dictionary'
    return (list(menu.keys())[list(menu.values()).index(max(menu.values()))],max(menu.values()))      # I only did this because it was funny


menuDict={'soup':12, 'salad':15,
           'hummus':10, 'fattoush':13, 'tabbouleh':17,
           'musakhan':32, 'maqluba':28, 'mansaf':40,
           'kibbeh':52, 'kebab':45, 'mandi':34, 'biryani':25,
           'pizza':19, 'burger':22, 'fries':12,
           'kunefe':15, 'cheesecacke':23, 'brownie':21}    

expensive_dish = maxMenu(menuDict)
print(f"The most expensive dish is {expensive_dish[0]} and it costs {expensive_dish[1]}QAR.")
