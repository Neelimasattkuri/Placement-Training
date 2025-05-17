l=[3,2,6,4,7,1,5]
max1=0
for i in l:
    if i>max1:
        max1=i
max2=0
for i in l:
    if i>max2 and i!=max1:
        max2=i
print(max1)