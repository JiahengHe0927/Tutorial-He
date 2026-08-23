#PB2

# ====================================
# Declaration part: 
# In most cases, the declaration part is at the top of the code.
# Mind the "magic numbers" in the code below, they are constants that are given in the problem description.
portion_down_payment=0.25
current_savings=0
r=0.04

total_month_a_year=12
half_month_a_year=6
# ====================================

annual_salary=float(input("Enter your annual_salary:"))
portion_saved=float(input("Enter percent of your salary to save, as a decimal:"))
total_cost=float(input("Enter the cost of your dream home:"))
semi_annual_raise=float(input("Enter the semi_annual raise,as a decimal:"))

# ====================================
# portion_down_payment=0.25
# r=0.04
# current_savings=0
# ====================================

months=0

# ====================================
# Using the variable we defined before.
monthly_salary=annual_salary/total_month_a_year
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

    # ====================================
    # Using the variable we defined before.
    if months % half_month_a_year == 0:
    # if months%6==0:
    # ====================================

        # ====================================    
        # Firstly, the indentation is 2 instead of 4 (same pattern in the code files)

        # Secondly, the expression can be simplified to one line, as shown below.
        annual_salary += annual_salary*semi_annual_raise
            # annual_salary=annual_salary+annual_salary*semi_annual_raise

            # monthly_salary=annual_salary/12
        monthly_salary = annual_salary/12
        # ====================================
    
print(months)