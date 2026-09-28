#1
cool = ["grey","green","blue"]
sortedcool = sorted(cool)
print(cool)
print(sortedcool)
#2
warm = ["yellow","orange"]
hot = ["red"]
brightcolors = warm
brightcolors.append(hot)
print(brightcolors)
hot.append("pink")
print(hot)
print(brightcolors)
#3
def mult(a,b):
    if b == 1:
        return a
    else:
        return a + mult(a,b-1)
print(mult(2,3))
#4
def fact(n):
    if n ==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))
#5
def mult(a,b):
    result=0
    while b >0:
        result+=a
        b-=1
    return result
print(mult(2,4))