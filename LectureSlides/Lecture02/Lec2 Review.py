pset_time = 15
sleep_time = 8
print(sleep_time > pset_time)

x=float(input("Enter a number for x:"))
y=float(input("Enter a number for y:"))
if x == y:
    print("x and y are equal")
    if y !=0:
        print("therefore,x/y is",x/y)
elif x < y:
    print("x is smaller,x/y is",x/y)
else:
    print("y is smaller,x/y is", x/y)
print("thanks")

mysum = 0
for i in range(7, 10):
    mysum += i
print(mysum)

mysum=0
for i in range (5,11,2):
  mysum += i
print(mysum)
