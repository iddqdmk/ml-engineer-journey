income = int(input("Enter your monthly income: "))
debts = int(input("Enter your monthly debts: "))

if income > 5000 and debts < 1000:
    print("LOW RISK")

elif income > 3000 and debts < 2000:
    print("MEDIUM RISK")

else:
    print("HIGH RISK")