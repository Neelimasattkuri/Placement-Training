l=[[1,3],[2,1],[3,2]]
k=2
n=len(l)
for i in range(k):
    for j in range(0,n-1-i):
        if l[j][1]>l[j+1][1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)