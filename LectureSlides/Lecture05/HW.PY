L=[9,6,0,3,2,1]

def index_sort(n):
    n=len(L)
    for i in range(n):
        min=i
        for j in range(i,n):
            if L[j]<L[min]:
                min=j
        L[i],L[min]=L[min],L[i]
        print(L)
    return L
# index_sort(L)

# [9,6,0,3]
# [0,6,9,3]
# [0,3,9,6]
# [0,3,6,9]


# Bubble sort
def bubble_sort(L):
    length = len(L)
    print("Original list is:", L)
    for j in range(length):
        for i in range(length-1-j):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                print(L)
        print("The ", j, "th biggest is now in the list")

bubble_sort(L)