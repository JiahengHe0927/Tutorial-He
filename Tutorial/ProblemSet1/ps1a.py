#PB1

# ====================================
# Declaration part: 
# In most cases, the declaration part is at the top of the code.
# Mind the "magic numbers" in the code below, they are constants that are given in the problem description.
portion_down_payment=0.25 # Global variable
current_savings=0
r=0.04

total_month_a_year=12
# ====================================

annual_salary=float(input("Enter your annual_salary:"))
portion_saved=float(input("Enter percent of your salary to save, as a decimal:"))
total_cost=float(input("Enter the cost of your dream home:"))

# ====================================
# portion_down_payment=0.25
# r=0.04
# current_savings=0
# ====================================

months=0 # Local variable

# ====================================
# Using the variable we defined before.
monthly_salary = annual_salary / total_month_a_year
# monthly_salary=annual_salary/12
# ====================================

down_payment=total_cost*portion_down_payment

while current_savings<down_payment:

    # ====================================
    # Using the variable we defined before.
    current_savings += current_savings*r/total_month_a_year + monthly_salary*portion_saved
    # current_savings=current_savings+current_savings*r/12
    # current_savings=current_savings+monthly_salary*portion_saved
    # ====================================

    # ====================================
    # Using better expression:
    months += 1
    # months=months+1
    # ====================================
    
print(months)