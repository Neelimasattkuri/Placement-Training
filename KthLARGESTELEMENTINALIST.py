l=[3,2,6,4,7,1,5]
k=4
n=len(l)
for i in range(k):
    for j in range(0,n-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l[-k])