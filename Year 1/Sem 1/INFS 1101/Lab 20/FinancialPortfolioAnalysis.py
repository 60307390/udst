def Validator(prompt):
    value = -1
    while value < 0:
        value = float(input(prompt))
        if value < 0:
            print("Please enter a positive number.")
    return value

def TotalAssets(cash, investments, real_estate, other_assets):
    return cash + investments + real_estate + other_assets

def TotalLiabilities(debts):
    return debts

def NetWorth(total_assets, total_liabilities):
    return total_assets - total_liabilities

def FinancialRecommendation(net_worth):
    if net_worth < 0:
        return "Consider debt counselling."
    elif 0 <= net_worth < 50000:
        return "Consider savings strategies."
    elif 50000 <= net_worth <= 500000:
        return "Consdier investment strategies."
    else:
        return "Consider wealth management services."

#Main Program
cash = Validator("Enter the value of Cash assets: ")
investments = Validator("Enter the value of Investment assets: ")
real_estate = Validator("Enter the value of Real Estate assets: ")
other_assets = Validator("Enter the value of Other assets: ")
debts = Validator("Enter the value of Debts: ")

total_assets = TotalAssets(cash, investments, real_estate, other_assets)
total_liabilities = TotalLiabilities(debts)
net_worth = NetWorth(total_assets, total_liabilities)
recommendatoin = FinancialRecommendation(net_worth)

print(f"Total Assets ${total_assets}")
print(f"Total Liabilities: ${total_liabilities}")
print(f"Net Worth: ${net_worth}")
print(f"Recommendation: {recommendation}")
