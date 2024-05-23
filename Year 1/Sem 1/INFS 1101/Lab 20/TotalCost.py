def calculate_total_cost(attendees, ticket_price):
    discount_rate = 0

    if attendees > 5:
        discount_rate = 0.1
    elif attendees > 10:
        discount_rate = 0.15

    total_cost = attendees * ticket_price
    discount = total_cost * discount_rate
    return total_cost - discount

#Main Program
ticket_price = 50

#User input for number of attendees
number_of_attendees = int(input("Enter the number of attendees: "))

#Calculate total cost
total_cost = calculate_total_cost(number_of_attendees, ticket_price)

#Output
print(f"Total cost for {number_of_attendees} attendees: ${total_cost}")
