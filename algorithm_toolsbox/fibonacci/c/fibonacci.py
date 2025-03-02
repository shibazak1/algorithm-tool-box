# compute nth fibonacci number
#written by viibug
#2024/7/29


def FibonacciRecursive(n):

    if n<=1:
        return n
    else:
        print(f"Compute the f{n} recursevly")
        return FibonacciSlow(n-1)+FibonacciSlow(n-2)





def FibonacciIerative(n):

    fibonacci = [0,1]

    for i in range(2,n+1):
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2]) 

    return fibonacci[n]

#---------------------------------------------------------------------------------------------

def FibonacciIerative2(n):
    previous,current = 0,1

    for i in range(2,n+1):
        previous,current = current, previous+current


    return current

#------------------------------------------------------------------------------------------------
table={}
def FibonacciRecursiveMemorization(n):

    if n not in table:
        if n<=1:
            table[n] = n
        else:
            table[n] = FibonacciRecursiveMemorization(n-1)+FibonacciRecursiveMemorization(n-2)
    return table[n]

    
    





n= input("Enter a Nth term")
print(FibonacciRecursiveMemorization(int(n)))
#print(f"fast result : {FibonacciIerative(int(n))}")
#print()
#print(f"slow result : {FibonacciRecursive(int(n))}")
