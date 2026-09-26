L=[9,6,0,3]
n=len(L)
for i in range(n):
    min=i
    for j in range(i,n):
        if L[j]<L[min]:
            min=j
    L[i],L[min]=L[min],L[i]
print(L)