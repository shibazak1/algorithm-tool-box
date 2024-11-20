


'''
Maximum Product of Two Sequences Problem Find the maximum dot product of two sequences of numbers.

Input: Two sequences of n positive integers: price1 , . . . , price n and clicks1 , . . . , clicks n .

Output: The maximum value of price1 · c1 + · · · + pricen · cn ,

where c1 , . . . , cn is a permutation of clicks1 , . . . , clicksn .
'''

#---------------------------------------------------------------------------------
import sys

# 2, 3 ,9
# 7, 4 ,2
def MaxDotsProduct(prices,clicks):

    # define the bese case where tow list is empty
    # in this case we have nothing to add so we return 0
    if not prices and not clicks:
        return 0

    #define the indcies of the max value becouse every call we cut the lists so it alwoyes start at 0
    max_price = 0
    max_click = 0
    #iterate over the list start at 1 index
    for i in range(1,len(prices)):
        # at every i we check if it is the max one in both list and tow list same leangth we are fine 
        if prices[i] >= prices[max_price]:
            max_price = i
        if clicks[i] >= clicks[max_click]:
            max_click = i

    #find the product
    product = prices[max_price] * clicks[max_click]

    #delete the items 
    prices.pop(max_price)
    clicks.pop(max_click)

    #call the function again
    return product + MaxDotsProduct(prices,clicks)
        
#---------------------------------------------------------------------
def MaxRevenue(prices,clicks):

    #define the revenue at the begining
    revenue = 0
    #loop over to find the maxs values unless the list is empty
    while len(prices) > 0:
        #finde the max value and assaign them 
        max_price = max(prices)
        max_click = max(clicks)

        #add the product of the new pair maxs to revenue
        revenue += max_click * max_price
        #delete them from the lists
        prices.remove(max_price)
        clicks.remove(max_click)
        
    return revenue

#--------------------------------------------------------------------
# the upper 2 function computer the max revenue in O(n^2)
# but if we sort the lists ahead we can do it in O(nlogn)

def MaxRevenueSorted(prices,clicks):
    prices , clicks = sorted(prices),sorted(clicks)

    #[prices[i]*clicks[i] for i in range(len(clicks))]
    #this will create a list of product p_i*c_i from and becouse we sort the 2 list
    # and return the sum of the new list by sum() function
    
    return sum([prices[i]*clicks[i] for i in range(len(clicks))])





#---------------------------------------------------------------------
if __name__ == '__main__':

    data = list(map(int,sys.stdin.read().split()))
    n = data[0]
    prices = data[1:n+1]
    clicks = data[n+1:]

    #print(f"{prices} \n {clicks}")
    print(MaxDotsProduct(prices,clicks))

    
