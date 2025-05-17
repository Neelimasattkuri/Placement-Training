
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r = len(m)
c = len(m[0])



for i in range(r):
    for j in range(c):
        num = m[i][j]
        if num > 1:
            is_prime = True
            for k in range(2, num):
                if num % k == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num)
