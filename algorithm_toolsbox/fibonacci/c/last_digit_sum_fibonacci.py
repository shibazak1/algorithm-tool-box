# last digit of sum of fibonacci number :
#defin as  S(n) = F(0)+F(1)+....+F(n-1)+F(n)
#last Digit of sum  is S(n) mod 10
#we find that S(n)= F(n+2)-1

# written by viibug
#at 2024/8/13

#----------------------------------------------------------------------------------------------------------------#
#                                       Last Digit Of Sum Of Fibonacci                                           #
#----------------------------------------------------------------------------------------------------------------#


def LastDigitFibonacci(n):
    current , nxt = 0,1 #first value of F(0) F(1)
    for _ in range(n):

        """
        keep track of last digit of F(n)
        if F(n) = F(n-2) + F(n-1) -> (next = current+next)
        and F(n)%10 = (F(n-2)%10 + F(n-1)%10) ->>

        f(n)/10 = k10+r
        f(n-2)/10 = k10 +r_2
        f(n-1)/10 = k10 +r_3

        so by summing and take the mod we do the same if we sum 1st
        we get

        f(n-2)+f(n-1) = (k10+10k) + (r_2+r_3) so the number will get bigger and give the same reminder insted

        by taking intermidiat mod 10

        the k10+k10 will removed and we remian with the r_2+r_3 that what we need becouse at last will removed
        so we removed first
        
        

        """
        current ,nxt = nxt,(current+nxt)%10

    return current





n = int(input("Enter n :"))
"""
S(n) = F(n+2)-1
compute f(n+2) mod 10
by take mod 60 the pisano period lenght
than add 9 insted of subtract 1 becouse -1 and 9 give the same remainder mod 10
then take another mod 10 to asure the number less then 10

"""
d =LastDigitFibonacci((((n+2)%60)+9)%10)
print(d)



#----------------------------------------------------------------------------------------------------------------#
#another solution


def multiply_2x2_matrices_mod10(a, b):
c = [[None] * 2 for _ in range(2)]
c[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % 10
c[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % 10
c[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % 10
c[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % 10
return c



def MatrixExponentMod10(d,n):

    if n==0:
        return [[1,0],[0,1]]

    elif n%2==0:
        z =MatrixExponentMod10(d,n//2)
        return multiply_2x2_matrices_mod10(z,z)
    else:
        z = MatrixExponentMod10(d,n//2)
        y = multiply_2x2_matrices_mod10(z,z)
        return multiply_2x2_matrices_mod10(z,d)




n = int(input("Enter n :"))
m = [[0,1],[1,1]]

d = MatrixExponentMod10(m,n+2)

print((d[0][1])%10)
        
