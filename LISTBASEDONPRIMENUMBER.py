l=[[20,12,11],[10,5,22],[16,7,30]]
n=len(l)
for i in range(n):
    for j in range(0,n-1-i):
        if l[j][1]>l[j+1][1]:
           l[j],l[j+1]=l[j+1],l[j]
print(l)