#clue:

#Money changeing problem is discribe the scenario when buy some thing whith price of 4.25$ and you pay whith 5%
#then the cachier should return to you (5 - 4.25) = 0.75$ whith the smalles amout of coin what ever denomeatore(value)


#problem statment:
"""
Change Problem

Convert some amount of money into given denominations, using the smallest
possible number of coins.

Input: An integer money and an array of d denominations
c = (c1 , c2 , . . . , cd ), in decreasing order of value (c1 > c2 > · · · > cd ).

Output: A list of d integers i1 , i2 , . . . , id such that c1 · i1 + c2 · i2 +
· · · + cd · id = money, and i1 + i2 + · · · + id is as small as possible
"""



#Implementations:

#imp(1)
def Change(money,c,d):

    #create list d of d zeros
    d = [0]*d
    #becouse the list of denomeatore is in decreasing order the 1st of is the largest coin
    index = 0
    # assign the the largest coin 
    coin = c[index]
    # inter loop of subtracting largest coin form money until we have no money
    while money!=0:
        #check if the coin is smaller than the money
        if money >= coin:
            #subtract it from money
            money = money-coin
            #increase the number if time we choose this coin at this index
            d[index] +=1
        else:
            #if the coin is larger we go to next one and asign it again 
            index +=1
            coin = c[index]

    return d # return the list 


#end imp(1)----------------------------------------------------------------

#imp(2):

def ChangeFast(money,c):
    d = []
    for k in range(len(c)):
        #insted of check every time whether this value is larger than money or not we may check the same
        #value maltiple time that slow down the program
        # instead we get how many time this coin fit in to the money which is fast version of cheching many time
        i = money//c[k] # give me number of coin if this denomeatore
        d.append(i) # add it to the list of d
        money = money - i*c[k] # decrease the money by freqauncy of the coin * value
    return d # returning the d


#end imp(2)----------------------------------------------------------------


#imp(3):
def BruteForceChange(money,c,d):
    #define smalles number of coin
    smallnc = 1000
    change  = [0]*d
    #iterate over all companations of c:
    for i in range(d):
        for k in range(d):
            for j in range(d):
                for d in range(d):
                    for l in range(d):
                        num_ith_coin = money//c[i]
                        num_kth_coin = money//c[k]
                        num_jth_coin = money//c[j]
                        num_dth_coin = money//c[d]
                        num_lth_coin = money//c[l]
                        print(num_ith_coin,num_kth_coin,num_jth_coin,num_dth_coin,num_lth_coin)
                        #calculate the value of the companation
                        value_of_coins = (num_ith_coin*c[i] + num_kth_coin*c[k] + num_jth_coin*c[j]+ num_dth_coin*c[l] + num_lth_coin*c[l])
                        print(value_of_coins)
                        #check if compoanation == money:
                        if money == value_of_coins:
                            #check if it is the smalles:
                            num_coins = num_ith_coin + num_kth_coin + num_jth_coin + num_dth_coin + num_lth_coin
                            if num_coins < smallnc:
                                #assaing it to the smallest varaible
                                smallnc = num_coins
                                change[i] += num_ith_coin
                                change[k] += num_kth_coin
                                change[j] += num_jth_coin
                                change[d] += num_dth_coin
                                change[l] += num_lth_coin



                            
    return change
                        
                        
                        
    
        
    
        
            
                
    


#end imp(3)----------------------------------------------------------------







money = 77
c = [25,20,10,5,1]
d = len(c)
#print(f"d = {Change(money,c,d)}")
#print(f"d = {ChangeFast(money,c)}")
print(f"d = {BruteForceChange(money,c,d)}")
