# 1. The python file should end with .py, in your original homework, the file only contains a name, without the .py

pi=3.14159
radius=2.2
area=pi*(radius**2)
print(area)

#Lecture 2
hi="hello there"

# 2. You dont run the python script, the >>> should not be included in the script, it is only used in the python shell to indicate that you are typing a command.

# >>> name = "ana"

# There is no space between hi and name, the "" contains no space. See the correct answer below. 
# >>> greeting = hi +""+ name

# >>> greeting
# By running the script, the following syntax error will be generated:
# File "/Users/yi1lan/Desktop/Students/Tutorial-He/LectureSlides/Lecture01/Lec1Review.py", line 10
#    >>> name = "ana"
#    ^^
# SyntaxError: invalid syntax

# The correct version should be:
name = "ana"
greeting = hi + " " + name # You should mind the space in the " "
greeting 
print(greeting)

silly=hi +""+name*3 # You should mind the space in the "", in your version, there is no space between hi and name, the "" contains no space. See the correct answer below.
silly
print(silly)

silly=hi + " " + name*3 
silly
print(silly)

x = 1
print(x)
x_str = str(x)
print("my fav num is", x, ".", "x =", x)
print("my fav num is " + x_str + ". " + "x = " + x_str)

import math

answer = 10
error = 0.001

g = float(input("Your guess is: "))

# if (math.fabs(g*g - answer) <= error):
#     print(g, " is the answer")
# else:
#     g = (g + answer/g)/2
#     print("Current result is: ", g)

while (math.fabs(g*g - answer) > error):
    g = (g + answer/g) / 2
    print("the current g is: ", g)

print(g, " is close enough")