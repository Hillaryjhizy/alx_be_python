#Script to calculate a user’s monthly savings based on inputted monthly income and expenses
#User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

#Calculating Monthly Savings
monthly_savings = monthly_income - monthly_expenses

#Projecting Annual Savings
interest_rate = 0.05

#annual_savings_without_interest = monthly_savings * 12
#annual_interest = annual_savings_without_interest * interest_rate
#projected_annual_savings = annual_savings_without_interest + annual_interest

Projected_anual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Output Results
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected annual savings after including interest are: ${Projected_anual_savings:.2f}")

