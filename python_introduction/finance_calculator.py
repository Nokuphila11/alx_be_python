def main():
  """Calculates and displays monthly and annual savings with interest."""

  # User Input
  monthly_income = float(input("Enter your monthly income: "))
  monthly_expenses = float(input("Enter your total monthly expenses: "))

  # Calculate Monthly Savings
  monthly_savings = monthly_income - monthly_expenses

  # Calculate Annual Savings with Interest
  annual_interest_rate = 0.05  # 5% annual interest rate (simplified)
  projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

  # Output Results
  print(f"Your monthly savings are: ${monthly_savings:.2f}")
  print(f"Your projected annual savings with interest are: ${projected_annual_savings:.2f}")

if __name__ == "__main__":
  main()
