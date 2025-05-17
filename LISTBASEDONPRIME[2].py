def is_prime(x):
    primes = []
    for i in x:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            primes.append(i)
    return sum(primes)
l=[[20,12,11],[10,5,22],[16,7,30,]]
b=[]
n=len(l)
for i in l:
    b.append(is_prime(i))
for i in range(n):
    for j in range(0,n-1-i):
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
            l[j],l[j+1]=l[j+1],l[j]
print(l)