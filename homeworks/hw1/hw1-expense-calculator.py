"""
Personal Finance Calculator
Student: [Tanawuttanun Homsilp]
Date: [27/07/2568]
Purpose: Calculate monthly budget and savings
"""
# กำหนดค่ารายรับรายจ่ายของตัวเองก่อน ละกำหนดเป็นสกุลเงิน(THB) และรับค่าจากคีบอร์ดองผ้ใช้
monthly_income = float(input("Enter your monthly income (THB): "))
rent_cost = float(input("Enter your monthly rent/housing cost (THB): "))
food_budget = int(input("Enter your monthly food budget (THB): "))
transportation_cost = float(input("Enter your monthly transportation cost (THB): "))
entertainment_budget = int(input("Enter your monthly entertainment budget (THB): "))
emergency_fund_percent = float(input("Enter emergency fund percentage (e.g., 10.5): "))
investment_percent = float(input("Enter investment percentage (e.g., 15.0): "))
# ใช้สตรคำนวณค่าใช้จ่าย + - * /
total_fixed_expenses = rent_cost + transportation_cost  
total_variable_expenses = food_budget + entertainment_budget  
total_expenses = total_fixed_expenses + total_variable_expenses  
remaining_income = monthly_income - total_expenses  
# คำนวณเงินออม
emergency_fund = monthly_income * (emergency_fund_percent / 100)  
investment_amount = monthly_income * (investment_percent / 100)  
available_for_savings = remaining_income - emergency_fund - investment_amount
# คำนวณสัดส่วนค่าใช้จ่ายต่อรายได้
expense_ratio = (total_expenses / monthly_income) * 100  
# แสดงค่าผลลัพธ์ที่คำนวณจากสูตรแล้ว
print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {total_fixed_expenses:.2f} THB")
print(f"Variable Expenses: {total_variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")
print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent}%): {emergency_fund:.2f} THB")
print(f"Investment ({investment_percent}%): {investment_amount:.2f} THB")
print(f"Available for Savings: {available_for_savings:.2f} THB")
print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")
