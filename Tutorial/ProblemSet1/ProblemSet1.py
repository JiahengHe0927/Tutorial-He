#PB1
annual_salary=float(input("Enter your annual_salary:"))
portion_saved=float(input("Enter percent of your salary to save, as a decimal:"))
total_cost=float(input("Enter the cost of your dream home:"))
portion_down_payment=0.25
r=0.04
current_savings=0
months=0
monthly_salary=annual_salary/12
down_payment=total_cost*portion_down_payment
while current_savings<down_payment:
    current_savings=current_savings+current_savings*r/12
    current_savings=current_savings+monthly_salary*portion_saved
    months=months+1
print(months)
 
#PB2
annual_salary=float(input("Enter your annual_salary:"))
portion_saved=float(input("Enter percent of your salary to save, as a decimal:"))
total_cost=float(input("Enter the cost of your dream home:"))
semi_annual_raise=float(input("Enter the semi_annual raise,as a decimal:"))
portion_down_payment=0.25
r=0.04
current_savings=0
months=0
monthly_salary=annual_salary/12
down_payment=total_cost*portion_down_payment
while current_savings<down_payment:
    current_savings=current_savings+current_savings*r/12
    current_savings=current_savings+monthly_salary*portion_saved
    months=months+1
    if months%6==0:
        annual_salary=annual_salary+annual_salary*semi_annual_raise
        monthly_salary=annual_salary/12
print(months)
 
 #PB3
starting_salary=float(input("Enter the starting salary:"))
total_cost=1000000
portion_down_payment=0.25
down_payment=total_cost*portion_down_payment
semi_annual_raise=0.07
r=0.04
low=0
high=10000
steps=0 
found=False
while low<=high:
    steps+=1
    mid=(low+high)/2
    portion_saved=mid/10000
    current_savings=0
    annual_salary=starting_salary
    monthly_salary=annual_salary/12
    for month in range(0,37,1):
        current_savings+=current_savings*r/12
        current_savings+=monthly_salary*portion_saved
        if month%6==0:
            annual_salary=annual_salary+annual_salary*semi_annual_raise
            monthly_salary=annual_salary/12
    if abs(current_savings-down_payment)<=100:
        found=True
        break
    elif current_savings<down_payment:
        low=mid+1
    else:
        high=mid-1
if found:
    print(portion_saved)
    print(steps)
else:
    print("It is not possible to pay the down payment in three years")