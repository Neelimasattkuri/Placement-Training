m=[
    [1,2,3],
    [4,5,6],
    [7,8,9]]
r=len(m)
c=len(m[0])
s=0
for i in range(r):
    for j in range(c):
        s+=m[i][j]
            
print(s)
        
