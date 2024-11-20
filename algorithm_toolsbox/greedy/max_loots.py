'''
Maximizing the Value of the Loot Problem
--------------------------
Find the maximal value of items that fit into the
backpack.

Input: The capacity of a back-pack W as well as the weights
(w1 , . . . , wn ) and costs (c1 , . . . , cn ) of n different compounds.

Output: The maximum total value of fractions of items that fit into the
backpack of the given capacity: i.e.,

the maximum value of c1 ·f1 +· · ·+cn ·
fn such that w1 · f1 + · · · + wn · fn ≤ W
and 0 ≤ fi ≤ 1 for all i (fi is the fraction of the i-th item taken to the
backpack).
'''


def MaximumeLoots(W,wights,costs):

    maxcost = 0
    while W>0:
        best_item = 0
        expensive_cost = 0
        
        for i in range(len(wights)):
                if wights[i] > 0 and costs[i]/wights[i] > expensive_cost:
                    expensive_cost = costs[i]/wights[i]
                    best_item = i
                    
                else:
                    continue
        
        amount_loot = min(wights[best_item],W)
        print(f"amount of the loot {amount_loot}")
        W -= amount_loot
        print(f"capasity {W}")
        maxcost += expensive_cost*amount_loot
        wights[best_item] -= amount_loot
        
    return maxcost


#---------------------------------------------------------------------------

def MaximumeLoots2(capacity,wights,values):
    #define the variable that hold the the cost of the loots in the bage
    # we want to maximize it
    value = 0

    while capacity>0:
        # repeat until the the bage get full 
        m = -1 # this is the the index of most expensive item

        for i in range(len(costs)):
            #search on the m
            
            if wights[i]>0:
                # cheack if there is no item becouse the item wight decrease
                
                if m == -1 or values[i]*wight[m] > values[m]*wight[i]:
                    # if the m not set yet or the price of the item per unit is more
                    # then the current m assighn the index to m
                    # Note: instead of useing fraction based comparation that take time
                    # values[i]/wight[i] > values[m]/wights[m]
                    # we use multiplication we know that the values[i] = price per unit*wight
                    # and we want to know wich item has most expensive price per unit
                    # so take the varaible values[]* wight[] of the other value
                    # by doing this eatch side of (>) will have the same term different by
                    # price per unit
                    # p_i * (w_i *w_m) > p_m * (w_m  * w_i) do you see the different
                    # the term with biggest p will win
                    m = i

        # if we exit the for loop with out setign the m mean all the wight is 0
        # there is nothing to put in the bage get out of  while loop an return value=0
        if m == -1:
            break


        # if we have 3 kg of item and the capcity 9 mean we can put the item in the bage
        # and if the remaining capcity of the bage 1 and the wight of  item 3
        # we can only take 1 kg of this item 
        amount = min(wight[m],capacity)
        value += amount * values[m] /wights[m]
        capacity -= amount
        wights[m] -= amount
        
#-----------------------------------------------------------------------------------------

def MaximumeLootsRecursive(capacity,wights,values):

    if  not capacity or not wights:
        return 0


    m = 0
    for i in range(1,len(wights)):
        if values[i]* wights[m] > values[m] * wights[i]:
            m=i

    amount  = min(wights[m],capacity)
    value = amount * values[m]/wights[m]
    wights.pop(m)
    values.pop(m)

    return value + MaximumeLootsRecursive(capacity,wights,values)









        

n,capacity_bag = map(int,input().split())
costs = [0]*n
wights = [0]*n

for i in range(n):
    costs[i] , wights[i] = map(int,input().split())

print(f"costs is {costs} , wight is {wights}")
print("{:.4f}".format(MaximumeLoots(capacity_bag,wights,costs)))
