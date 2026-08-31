
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


annual_salary=float(input("Enter the starting salary:"))
monthly_salary=annual_salary/total_month_a_year

annual_salary_minimum=annual_salary
monthly_salary_minimum=monthly_salary



minimum_portion = 1

for month in range(1, plan_month+1, 1):
    
    current_savings += current_savings*r/total_month_a_year + monthly_salary*minimum_portion

 
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
     
    
    current_rate = (low + high) // 2
    current_savings=0

    for month in range(1, plan_month+1, 1):
       
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