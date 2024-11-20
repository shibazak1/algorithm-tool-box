
#implementation of linear search


def LinearSearchRecursive(array,low,high,k):

    #there tow base case when k does not exist and low will be = high
    #or when we found the k and return the index low
    if high<low:
        return "not found"
    if array[low] == k:
        return low

    #if none of both cases is resolve call the function with increase the low index
    #by this at eatch we deacres the problem
    return LinearSearchRecursive(array,low+1,high,k)
#-----------------------------------------------------------------------------------------

def LinearSearchIterative(array,low,high,k):

    for i in range(low,high):
        if array[i] == k:
            return i
    return "not found"


array = [2,3,4,6,8,41,77]
k = 4
print(LinearSearchRecursive(array,0,len(array)-1,k))

