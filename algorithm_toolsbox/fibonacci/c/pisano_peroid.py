#find the pisano peroid (the length of sequens of Fi mod m)

#written by viibug

# 2024/8/7



def PisanoPeroid(modulus):
#start with first and second fibonacci and compute the mod until the first pair is repeat
    
    a =0
    b= 1
    count = 0
    
    while True:
        
        a , b = b , (a+b) % modulus # a = 1 , b = 0+1%m = 1
        count +=1
        if a==0 and b == 1:
            return count



def FibonacciMod(n,m):

    a,b = 0,1

    for i in range(n):

        a,b = b, (a+b)%m
    return a # return a becouse at n cycle a will be the previous b and b = a+b the next a






        
        

n,m = map(int, input("Enter n , m").split())

print(FibonacciMod(n%PisanoPeroid(m),m))



