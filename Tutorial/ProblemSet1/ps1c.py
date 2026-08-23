 #PB3

# ====================================
# Declaration part: 
# In most cases, the declaration part is at the top of the code.
# Mind to separate the line for readability. 
# Mind the "magic numbers" in the code below, they are constants that are given in the problem description.
total_cost=1000000
current_savings=0

portion_down_payment=0.25
down_payment=total_cost*portion_down_payment

r=0.04
semi_annual_raise=0.07

total_month_a_year=12
half_month_a_year=6

low=0
high=10000
# ====================================

starting_salary=float(input("Enter the starting salary:"))

# ====================================
# total_cost=1000000
# portion_down_payment=0.25
# down_payment=total_cost*portion_down_payment
# semi_annual_raise=0.07
# r=0.04
# low=0
# high=10000
# ====================================

steps=0 
found=False

# Re-write the calculation part. 
# while low<=high:
#     steps+=1
#     mid=(low+high)/2
#     portion_saved=mid/10000
#     current_savings=0
#     annual_salary=starting_salary
#     monthly_salary=annual_salary/12
#     for month in range(0,37,1):
#         current_savings+=current_savings*r/12
#         current_savings+=monthly_salary*portion_saved
#         if month%6==0:
#             annual_salary=annual_salary+annual_salary*semi_annual_raise
#             monthly_salary=annual_salary/12
#     if abs(current_savings-down_payment)<=100:
#         found=True
#         break
#     elif current_savings<down_payment:
#         low=mid+1
#     else:
#         high=mid-1
# if found:
#     print(portion_saved)
#     print(steps)
# else:
#     print("It is not possible to pay the down payment in three years")