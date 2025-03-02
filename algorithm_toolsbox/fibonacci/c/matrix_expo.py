#finding F(n) using matrix multiplication in 2log(n) timer

#written by viibug

#2024/8/12


#----------------------------------------------------------------------------------------------#
#                                <Fast matrix Exponentiation>                                  #
#----------------------------------------------------------------------------------------------#
def Multiply2x2Matrcies(a,b,m):

    c = [[None]*2 for _ in range(2)]

    c[0][0] = (a[0][0]*b[0][0] + a[0][1]*b[1][0])%m
    c[0][1] = (a[0][0]*b[0][1] + a[0][1]*b[1][1])%m

    c[1][0] = (a[1][0]*b[0][0] + a[1][1]*b[1][0])%m
    c[1][1] = (a[1][0]*b[0][1] + a[1][1]*b[1][1])%m
    

    return c


def FastMatrixExponentiation(a,n,m):

    if n==0:
        return [[1,0],[0,1]]

    elif n%2==0:
        z = FastMatrixExponentiation(a,n//2,m)
        return Multiply2x2Matrcies(z,z,m)
    
    else:
        z = FastMatrixExponentiation(a,n//2,m)
        y = Multiply2x2Matrcies(z,z,m)
        return Multiply2x2Matrcies(a,y,m)




n, m = map(int,input("Enter n , m : ").split())

a = [[0,1],[1,1]]

d = FastMatrixExponentiation(a,n,m)

print(d[0][1])

