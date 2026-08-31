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

plan_month = 36

low=0
high=10000
decimal=10000

error=100 
# ====================================

# ====================================
# 1 iteration 
# low = 0; high = 10000;
# calculate mean: 5000 => how is your saving?
# if saving > 1M + 100:
#    low = 0; high = 5000
# elif saving < 1M - 100:
#    low = 5000; high = 10000;
# (assume saving < 1M)

# 2 iteration
# low = 5000; high=10000
# calculate mean: 7500 => how is your saving?
# if saving > 1M + 100:
#    low = 5000; high = 7500
# elif saving < 1M - 100:
#    low = 7500; high = 10000

# ... iteration
# until: when using some mean, 1M - 100 <= saving <= 1M + 100
# return mean / 10000 
# ====================================

annual_salary=float(input("Enter the starting salary:"))
monthly_salary=annual_salary/total_month_a_year

annual_salary_minimum=annual_salary
monthly_salary_minimum=monthly_salary

# ====================================
# total_cost=1000000
# portion_down_payment=0.25
# down_payment=total_cost*portion_down_payment
# semi_annual_raise=0.07
# r=0.04
# low=0
# high=10000
# ====================================

minimum_portion = 1

for month in range(1, plan_month, 1):
    # Calculate monthly saving 
    current_savings += current_savings*r/total_month_a_year + monthly_salary*minimum_portion

    # Raise salary every half a year 
    if month % 6 == 0:
        annual_salary_minimum += annual_salary_minimum * semi_annual_raise
        monthly_salary_minimum = annual_salary_minimum / total_month_a_year

if current_savings < down_payment - error:
    print("It is not possible to pay the down payment in three years.")
    exit()

step=0

while (current_savings < down_payment - error) or (current_savings > down_payment + error): 

    annual_salary_iterate = annual_salary
    monthly_salary_iterate = annual_salary_iterate / total_month_a_year
     
    # current_rate_wrong = (low + high) / 2
    current_rate = (low + high) // 2
    current_savings=0

    for month in range(1, plan_month, 1):
        # Calculate monthly saving 
        current_savings += current_savings*r/total_month_a_year + monthly_salary_iterate*(current_rate/decimal)

        if month % 6 == 0:
                annual_salary_iterate += annual_salary_iterate * semi_annual_raise
                monthly_salary_iterate = annual_salary_iterate / total_month_a_year

    if current_savings > down_payment + error:
         high=current_rate
    elif current_savings < down_payment - error:
         low=current_rate
    step+=1

    print("Current rate is: ", current_rate)

print("Best savings rate: ", (current_rate/decimal))
print("Steps in bisection search: ", step)     