monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

annual_interest_rate = 0.05  # Annual interest rate

Projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate))

print(f"Your monthly savings are ${monthly_savings}.")

print(f"Projected savings after one year, with interest, is: ${Projected_savings}.")