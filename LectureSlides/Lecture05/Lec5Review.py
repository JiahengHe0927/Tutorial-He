# # Example 1 
# x = input("Enter a number:") 
# y = input("Enter a number:") 

# print("x is:", x, "; y is:", y)

# (y, x) = (x, y)

# print("x is:", x, "; y is:", y)


# # Example 2 
# def quotient_and_remainder(x, y):
#     q = x // y
#     r = x % y
#     return (q, r)

# (quot, rem) = quotient_and_remainder(4,5)
# print(quot, rem)
# print((quot, rem))


# # Example 3
# aTuple = ( (3, "abc"), (4, "def"), (7, "gh"), (1, "abc"), (2, "ab") )

# def get_data(aTuple):
#     nums = ()
#     words = ()
#     for t in aTuple:
#         nums = nums + (t[0],)   
#         if t[1] not in words:   
#             words = words + (t[1],)
#     min_n = min(nums)
#     max_n = max(nums)
#     unique_words = len(words)
#     return (min_n, max_n, unique_words)

# (min_n, max_n, unique_words) = get_data(aTuple)
# print((min_n, max_n, unique_words))


# Example 4 

L = [2,5,3,4]

total = 0 
for i in range(len(L)): 
    print("In loop 1, i is:", i)
    total += L[i] 
print(total)

total = 0 
for i in L: 
    print("In loop 2, i is:", i)
    total += i
print(total)