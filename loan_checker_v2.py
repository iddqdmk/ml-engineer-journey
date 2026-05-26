def calculate_risk(income, debts, credit_score):

    reasons = []

    score = 0

    if income >= 5000:
        score += 2
    else:
        reasons.append("Low income")

    if debts <= 1000:
        score += 2
    else:
        reasons.append("High debts")

    if credit_score >= 700:
        score += 2
    elif credit_score >= 600:
        score += 1
    else:
        reasons.append("Low credit score")

    if score >= 5:
        return "LOW RISK", reasons
    elif score >= 3:
        return "MEDIUM RISK", reasons
    else:
        return "HIGH RISK", reasons


try:
    income = float(input("Income: "))
    debts = float(input("Debts: "))
    credit_score = int(input("Credit score: "))

    risk, reasons = calculate_risk(income, debts, credit_score)

    print("Risk level:", risk)

    if reasons:
        print("Reasons:")
        for r in reasons:
            print("-", r)

except ValueError:
    print("Invalid input")