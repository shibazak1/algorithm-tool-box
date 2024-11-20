# how to find the   x^n in O(log n) time
# writen by viibug
# 2024/8/11


def FastIntegerExponentiation(x,n):

    """
    x^9 = x^8*x
    x^8 =  x^4 *x^4
    x^4 = x^2 *x^2
    x^2 = x*x  
    x = x^0  >> 1
    x^0 = 1

    if n==0:   # here X^n = 1
        return 1

    elif n%2==0: # n is even like x^8 = x^4 *x^4 
        y = FastIntegerExponentiation(x,n/2)
        return y*y
    else:
        y = FastIntegerExponentiation(x,n-1) # n is odd x^9 = x *x^8
        return y*x


    
        


