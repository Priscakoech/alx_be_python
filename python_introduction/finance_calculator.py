monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
annual_savings_without_interest = monthly_savings * 12
annual_savings_with_interest = annual_savings_without_interest + (annual_savings_without_interest * 0.05)
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings_with_interest:.2f}.")