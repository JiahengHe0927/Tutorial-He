# # Example 1. 
# def Febonacci(n):
#     # Base case:
#     if n == 1 or n == 2:
#         return 1 
#     # Recursion:
#     return Febonacci(n - 1) + Febonacci(n - 2)

# # 1: 1 
# # 2: 1
# # 3: 1 + 1 = 2
# # 4: 1 + 2 = 3 
# # 5: 2 + 3 = 5 
# # 6: 3 + 5 = 8 
# # 7: 5 + 8 = 13
# print(Febonacci(7))


# # Example 2. 
# def factorial(n):
#     if n == 0:
#         return 1 
#     return n * factorial(n - 1)

# def factorial2(n):
#     if n == 0:
#         return 1 
#     result = 1 
#     for i in range(1, n + 1):
#         result *= i 
#     return result

# # 0! = 1 
# # 1! = 1 * 0!
# # 2! = 2 * 1!
# # 3! = 3 * 2!
# # 4! = 4 * 3!
# # ...
# # n! = n * (n-1)! = n * (n - 1) *  (n - 2) * ... * 1 
# print(factorial(5))
# print(factorial2(5))


# # Example 3 (Memorization). 
# def fib(n):
#     return go(n, 0, 1)

# # x is the first term; y is second term
# # n is the counter
# def go(n, x, y):
#     # Base case
#     if n == 0:
#         return x 
#     return go(n - 1, y, x + y)

# # (x, y), x + y 
# # x, (y, x + y)

# print(fib(7))

# # fib(3) = go(3, 0, 1)
# #        = go(2, 1, 1)
# #        = go(1, 1, 2)
# #        = go(0, 2, 3)
# #        = 2

# # fib(7) = go(7, 0, 1)
# #        = go(6, 1, 1)
# #        = go(5, 1, 2)
# #        = go(4, 2, 3)
# #        = go(3, 3, 5)
# #        = go(2, 5, 8)
# #        = go(1, 8, 13)
# #        = go(0, 13, 21)
# #        = 13

# # 1: 1 
# # 2: 1
# # 3: 1 + 1 = 2
# # 4: 1 + 2 = 3 
# # 5: 2 + 3 = 5 
# # 6: 3 + 5 = 8 
# # 7: 5 + 8 = 13


# # Example 4. 
# def isPal(s):
#     if len(s) <= 1:
#         return True
#     else:
#         return s[0] == s[-1] and isPal(s[1:-1])

# # isPal("abccba")
# # = a == a and isPal("bccb")
# # isPal("bccb")
# # = b == b and isPal("cc")
# # isPal("cc")
# # = c == c and isPal("")

# # isPal("abccda")
# # = a == a and isPal("bccd")
# # isPal("bccd")
# # = b == d and isPal("cc")
# # isPal("cc")
# # = c == c and isPal("")


# # Example 5. 
# my_dict = {}

# # Construction (to define a dictionary)
# grades = {
#     # key: value
#     'Ana': 'A+',
#     "John": 'B',
#     "Denise": 'A',
#     "Katy": 'A',
# }

# # print(grades['John'])

# # Add an entry into dictionary
# grades["Sylvan"] = 'A'

# # del(grades['Ana'])
# # print(grades)

# print(grades.keys())
# print(grades.values())


# # Example 6. 
# def fib_efficient(n, dict):
#     if n in dict:
#         return dict[n]
#     else:
#         ans = fib_efficient(n-1,dict) + fib_efficient(n-2, dict)
#         dict[n] = ans 
#         return ans 
    
# Fib_num = {1:1, 2:1}
# print(fib_efficient(6, Fib_num))

# # fib_efficient(3, dict)
# # ans = fib_efficient(2, dict) + fib_efficient(1, dict)
# #     = 1 + 1 = 2

# # Memorization via Dictionary
# # 
# # fib_efficieint(6, dict) => dict[6] = 8
# # ans = fib_efficient(5, dict) + fib_efficient(4, dict)
# # To calculate fib_efficient(5, dict): => dict[5] = 5
# # ans' = fib_efficient(4, dict) + fib_efficient(3, dict)
# # To calculate fib_efficient(4, dict): => dict[4] = 3
# # ans'' = fib_efficient(3, dict) + fib_efficient(2, dict)
# # To calculate fib_efficient(3, dict): => dict[3] = 2
# # ans''' = fib_efficient(2, dict) + fib_efficient(1, dict)


# Example 7.
sentence = "This is a sentence"
for word in sentence:
    print(word)