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


# # Example 4 
# # Via index
# L = [2,5,3,4]

# total = 0 
# for i in range(len(L)):    # i from 0 to 3 (0, 1, 2, 3)
#     print("In loop 1, i is:", i)
#     total += L[i] 
# print(total)

# # Via item 
# total = 0 
# for i in L:                # i is element in L (2, 5, 3, 4)
#     print("In loop 2, i is:", i)
#     total += i
# print(total)


# # Example 5
# L1 = [2, 5, 3, 4]
# print("Original list is (L1): ", L1)

# # Add an element into a list
# L1.append(7)
# print("After appendix we have (L1): ", L1)

# # Concat
# L2 = [1, 2, 3]
# L3 = L1 + L2
# print("After concat we have (L3): ", L3)

# # Using extend to add elements
# L1.extend([0, 6])
# print("After extend we have (L1): ", L1)

# # Delete
# # 1. Using index in list
# del(L1[1])
# print("After del we have (L1): ", L1)

# # 2. Using pop
# last_element = L1.pop()
# print("After pop we have (L1): ", L1)
# print("The last element pop is: ", last_element)

# # Pop iteration
# print("Inside iteration")
# for i in range(3):
#     a = L1.pop()
#     print("After pop we have (L1): ", L1)
#     print("The last element pop is: ", a)

# # 3. Using remove()
# L1.remove(2)
# print("After remove we have (L1): ", L1)

# L4 = [2, 2, 3, 3, 4]
# L4.remove(2)
# print(L4)


# # Example 6. 
# s = "I<3 cs"
# # list(s)
# # print(list(s))
# s.split('<')
# # print(list(s))
# print(list(s.split('<')))
# print(s)


# Example 7. 
L = ['a', 'b', 'c']
print(''.join(L))
print(' '.join(L))
print('_'.join(L))
print('123'.join(L))
