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