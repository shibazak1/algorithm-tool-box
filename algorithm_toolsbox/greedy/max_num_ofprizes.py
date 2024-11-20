


"""
Distinct Summands Problem
Represent a positive integer as the sum of the maximum number of pairwise distinct positive integers.
Input: A positive integer n
.
Output: The maximum k such that n can be represented as the sum a1 + · · · + ak of k distinct positive integers.
"""


def MaxOfK(n):

    knum = []
    a = 0
    while sum(knum) <= n:
        a+=1
        knum.append(a)
        
    knum = knum[:len(knum)-1]
    if sum(knum)<n:
        knum[-1] += n-sum(knum)
    return knum


#-------------------------------------------------------------------------

def get_prize(n):

    # to know if k numbers (a1+...+ak) can represent n the sum if all k numbers most be <= n
    # becouse if sum of all k > n that mean n will take part of the sequance and the other part become empty
    # so the sum of k numbers must be <= n so n can be freely distributed
    # in this while we goe far enough to get the largest k possible this while loop will exced the right value by1
    # we most goe backword 1 time
    # n=6 ,k=4 ,sum([1,2,3,4]) = 10, remove 4 , k = 3
    k=1
    while (k*(k+1))//2 <= n:
        print("k = ",k)
        k +=1
    print("k is",k)
    k -=1
    print("k = ",k)

    
    delta = n - (k*(k+1))//2
    print("delta = ",delta)
    # that will generate list of [1,2,...,k-1] so we add the what is remain to get = n
    return list(range(1,k)) + [k+delta]
    

n = input("enter n:")
#print(get_prize(int(n)))
print(MaxOfK(int(n)))

    
