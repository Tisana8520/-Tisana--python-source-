"""
Personal Finance Calculator
Student: [Your Name]
Date: [Today's Date]
Purpose: Calculate monthly budget and savings

"""

monthly_income = float(input("รายได้ต่อเดือน (THB): "))
rent_cost = float(input("ค่าเช่า (THB): "))
transportation_cost = float(input("ค่าเดินทาง (THB): "))
food_budget = int(input("ค่ากิน (THB): "))
entertainment_budget = int(input("ค่าพักผ่อน (THB): "))
emergency_fund_percent = float(input("เงินฉุกเฉิน (%): "))
investment_percent = float(input("เงินลงทุน (%): "))
print("\n===================================================")
    
total_fixed_expenses = rent_cost + transportation_cost
total_variable_expenses = food_budget + entertainment_budget
total_expenses = total_fixed_expenses + total_variable_expenses
remaining_income = monthly_income - total_expenses

emergency_fund_amount = monthly_income * (emergency_fund_percent / 100)
investment_amount = monthly_income * (investment_percent / 100)
available_for_savings = remaining_income - emergency_fund_amount - investment_amount

expense_ratio = (total_expenses / monthly_income) * 100

print("\n===========================")
print("|| MONTHLY BUDGET REPORT || ")
print("===========================")
print(f"\nRemaining Income: {monthly_income:.2f} THB")
print(f"Total Expenses: {total_fixed_expenses:.2f} THB")
print(f"Total Variable Expenses: {total_variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")
print("\n===================================================")

print("\n=======================")
print("|| SAVINGS BREAKDOWN ||")
print("=======================")
print(f"\nEmergency Fund Amount ({emergency_fund_percent}%): {emergency_fund_amount:.2f} THB")
print(f"Investment Amount ({investment_percent}%): {investment_amount:.2f} THB")
print(f"Available for Savings: {available_for_savings:.2f} THB")
print("\n===================================================")

print("\n===============")
print("|| ANALYSIS || ")
print("===============")
print(f"\nExpense Ratio: {expense_ratio:.2f}%")
print("\n===================================================")