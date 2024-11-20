#given n compute the [(F(0))^2 + (F(1))^2 +...+(F(n))^2 ]%10

#insted of squar every term we that will be very slow and the numebr will be large
# we found that this (F(0))^2 + (F(1))^2 +...+(F(n))^2  = F(n)*F(n+1)


def sum_squar_fibonacci(n):

    n = n%60

    current ,nxt = 0,1

    for _ in range(n):
        current , nxt = nxt ,(current+nxt)%10

    return((current*nxt)%10)





n = int(input("Enter n: "))

print(sum_squar_fibonacci(n))


