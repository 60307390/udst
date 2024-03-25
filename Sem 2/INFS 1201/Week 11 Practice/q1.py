import random, math

def create_random_bills(num):
    bills = []
    for i in range(num):
        bills.append(random.randint(1e3,1e4)/1e2)
    return bills

def badr(bills):
    bills_total = 0
    for i in bills:
        bills_total += i
    return math.floor(bills_total), round(bills_total), math.ceil(bills_total)

def jassim(bills):
    bill_floor = []
    bill_round = []
    bill_ceil = []
    for i in bills:
        bill_floor.append(math.floor(i))
        bill_round.append(round(i))
        bill_ceil.append(math.ceil(i))
    return sum(bill_floor), sum(bill_round), sum(bill_ceil)

bills = create_random_bills(30)
print(bills)
print('-------------------')
print(badr(bills))
print('-------------------')
print(jassim(bills))