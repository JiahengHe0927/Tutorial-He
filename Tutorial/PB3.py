starting_salary=float(input("Enter the starting salary:"))
annual_salary=starting_salary
total_cost=1000000
portion_down_payment=0.25*total_cost
deviation=100
def calculate_savings(annual_salary,portion_saved):
    current_savings=0
    r=0.04
    semi_annual_raise=0.07
    monthly_salary=annual_salary/12
    for month in range(1,37,1):
      if month%6==0:
          annual_salary=annual_salary+annual_salary*semi_annual_raise
          monthly_salary+annual_salary/12
          current_savings+=current_savings*r/12
max_savings=calculate_savings(starting_salary,1)
if max_savings<portion_down_payment-deviation:
    print("It is not possible to save for the down payment in 36 months.")
else:
    low=0
    high=10000
    steps=0
    while high-low>1:
        steps+=1
        current_rate=(low+high)/2
        savings=calculate_savings(starting_salary,current_rate/10000)
        if savings>down_payment+deviation:
            high=current_rate
        elif savings<down_payment-deviation:
            low=current_rate
        else:
            break
            best_rate=(low+high)/2/10000
            print(best_rate)
            print(steps)