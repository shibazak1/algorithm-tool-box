#find the Greatest commen divisor of a,b
#written by viibug
#in 2024/8/23


#----------------------------------------------------------------------------------------------#
#                                         GCD                                                  #
#----------------------------------------------------------------------------------------------#


def gcd_naive(a,b):

    # we iterate the smallest of a,b becouse id a<b and d|a,b then d most be <=a lage number can
    #not divide smaller on
    #this algo is to slow if a=10^9 and b=10^9 +1 it will preform 10^9 division in worst case
    
    for d in min(a,b):
        if a%d==0 and b%d==0:
            return d


#-----------------------------------------------------------------------------------------------------------------
def gcd_slow(a,b):


    """

    we found that if d | a,b then d|a-b ,b
    proof :-
    if d | a,b then a,b leave remiander of 0 when divided by d so
    a,b can be written as

    a = dq ,b = dk
    a-b  = dq-dk => d(q-k)

    a = q time of d => d(1)+d+d+d......d(q)
    b = k  time  of d=> d(1)+d+d+d+d......d(k)

    if we take a form b what will remain is also a muliple of d

    by reapeting this one of a ,b will become zero andother is the d
    
    """


    while a>0 and b>0:
        if a>=b:
            print(f"a is {a} b is {b} : {a}-{b} is ")
            a = a-b
            print(a)
        else:
            print(f"a is {a} b is {b} : {b}-{a} is ")
            b = b-a
            print(b)
    return max(a,b)






#-----------------------------------------------------------------------------------------------------
def EuclideIterative(a,b):
    """
    we notice that what we do when we take as mutch b from a we get the remainder when a/b
    so we will skip so mutch work by take a mod b insted of a-b
    
    """

    while a>0 and b>0:

        if a>=b:
            print(f"a is {a} b is {b} : {a}mod{b} is ")
            a = a%b
            print(a)
        else:
            print(f"a is {a} b is {b} : {b}mod{a} is ")
            b = b%a
            print(b)
    return max(a,b)



#-------------------------------------------------------------------------------
def EcluideRecursive(a,b):

    if a==0 or b ==0:
        return max(a,b)
    else:
        #by switching a,b  a = b and b = a%b so the new b will be smaler then original b
        return EcluideRecursive(b,a%b)









a,b  = map(int,input("Enter a ,b").split())

print(Euclide(a,b))


