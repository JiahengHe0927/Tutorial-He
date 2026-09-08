# this is a comment 1
# this is a comment 2 

"""
This is a comment line 1
This is a comment line 2
"""

# def a_add_one_times_two(i):
#     """
#     Input: None 
#     Output: a add one 
#     """
#     i += 1 
#     i *= 2
#     print("Adding one and times two")
#     return i 

# def a_add_one(i):
#     i += 1 
#     print("Adding one only")
#     return i 

# def a_time_two(i):
#     i *= 2 
#     print("Time two only")
#     return i 

# a = 5 
# print("Before function: a = ", a)

# a = a_add_one_times_two(a)

# print("After function: a = ", a)
# print("\n\n")


# a = 5 
# print("Before function: a = ", a)

# b = a_add_one(a)
# print("Inside function: b = ", b)
# print("Inside function: a = ", a)

# c = a_time_two(b)
# print("After function: c = ", c)
# print("After function: a = ", a)
# print("After function: b = ", b)

"""
def two_times(x):
    return x * 2

a = two_times(3)
"""

# def is_even(i):
#     print("Inside is_even")
#     return i % 2 == 0 

# is_even(3)

# def f(x):
#     x += 1 
#     print("in f(x) x = ",  x)
#     return x 
#     print("aaaa")
#     print("bbb")

# x = 3 
# z = f(x)

# print("now x is : ", x, ", and z is: ",z)

# def no_return(x):
#     x += 1 

# a = no_return(3)

# print("a is: ", a)

# def func_a():
#     print('inside func_a')

# def func_b(y):
#     print('inside func_b')
#     return y

# def func_c(z):
#     print('inside func_c')
#     return z()

# print(func_a())
# # inside func_a
# # None

# print(5+func_b(2))
# # inside func_b
# # 7 

# print(func_c(func_a))
# # inside func_c
# # inside func_a
# # None

# def f(y):
#     x = 1
#     x += 1
#     print(x)

# x = 5
# f(x)
# print(x)

# def g(y):
#     print(x)
#     print(x+1)

# x = 5
# g(x)
# print(x)

def h(y):
    pass
    # x += 1 #leads to an error without line `global x` inside h
    
x = 5
h(x)
print(x)