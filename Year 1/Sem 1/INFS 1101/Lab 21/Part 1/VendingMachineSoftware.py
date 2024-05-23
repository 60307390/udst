def vending_machine_operation(credit, item_cost):
    items_purchased = 0

    while credit >= item_cost:
        decision = input("Do you want to buy an item? (yes/no): ").lower()
        if decision == 'yes':
            credit -= item_cost
            items_purchased += 1
            print(f"Item purchased. Remaining credit: ${credit}")
        elif decision =='no':
            break

    return items_purchased

# Main Program
user_credit = float(input("Enter your credit amount: $"))
cost_per_item = 1.5

# Vending Machine Operation
total_items = vending_machine_operation(user_credit, cost_per_item)

# Output
print(f"Total items purchased: {total_items}")
print(f"Remaining credit: ${user_credit}")
