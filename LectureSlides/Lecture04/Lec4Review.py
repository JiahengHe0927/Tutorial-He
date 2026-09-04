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

def is_even(i):
    print("Inside is_even")
    return i % 2 == 0 

is_even(3)