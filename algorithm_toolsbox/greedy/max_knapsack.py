
# given W a capacity of a bag and array of w1,v1,...wn,vn to be the waight and the value (cost)
# of losts develop an algorithm to maximize the value of the lots taken in to the bag where
# whight of the lost does not exceed the capacity of the knapsack


def BestItem(lots):

    best_value = 0
    best_item_idx = 0

    for i in range(len(lots)-1):
        if lots[i+1]>0:
            unit_value = lots[i]/lots[i+1]
            if unit_value > best_value:
                best_item_idx = i+1
                best_value = unit_value
            
    return best_item_idx
    
    




def Knapsack(W,lots):

    amounts = [0]*len(lots)
    total_value = 0
    
    for i in range(len(lots)):
        if W==0:
            return (amounts,total_value)
        
        w_i = BestItem(lots)
        a = min(lots[w_i],W)
        total_value += a*(lots[w_i-1]/lots[w_i])
        amounts[w_i-1] = a*(lots[w_i-1]/lots[w_i])
        amounts[w_i] = amounts[w_i]+a
        lots[w_i] = lots[w_i] - a
        W -= a
    return (amounts,total_value)
        
        

loots = [30,5,28,4,24,3]
#amounts, total_value = Knapsack(9,loots)
#print(amounts,total_value)
print(Knapsack(9,loots))
