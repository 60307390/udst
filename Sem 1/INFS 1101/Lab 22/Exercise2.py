def process_order():
    def calculate_item_cost(item, quantity):
        price_per_item = 0

        if item == "burger":
            price_per_item = 5
        elif item == "pizza":
            price_per_item = 7
        elif item == "salad":
            price_per_item = 4
        else:
            print("Item not recognized. Price set to 0.")
        
        return price_per_item * quantity

    total_cost = 0
    order_more = True

    while order_more:
        item = input("Enter the item name (burger, pizza, salad): ").lower()
        quantity = int(input("Enter the quantity: "))

        item_cost = calculate_item_cost(item, quantity)
        total_cost += item_cost

        print(f"Cost for {quantity} {item}(s): ${item_cost}")

        choice = input("Do you want to order more items? (yes/no): ").lower()
        if choice == "no":
            order_more = False

    return total_cost

# Main Program
total_order_cost = process_order()
print(f"Total order cost: ${total_order_cost}")
