a=[7,8,9,1,2,3,4,5,6]
l=0
r=len(a)-1
while l<=r:
    mid=(l+r)//2
    if a[mid]>a[mid+1]:
        res=mid
        break
    if a[mid]<a[mid-1]:
        res=mid
        break
    if a[mid]<a[mid-1]:
        res=mid-1
        break
    if a[l]>=a[mid]:
        r=mid-1
    else:
        l=mid+1
print(res)