m=[[1,0,0,1],
   [1,0,0,0],
   [0,0,1,0],
   [0,1,1,0]]
a=[5,10,3,4]
for i in range(len(m)):
    sum=0
    for j in range(len(m[0])):
        if m[i][j]==1:
            sum+=a[j]
    print(sum)