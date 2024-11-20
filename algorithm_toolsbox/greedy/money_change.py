'''
Money Change Problem

Compute the minimum number of coins needed
to change the given value into coins with denomi-
nations 1, 5, and 10.

Input: An integer money.

Output: The minimum number of coins with denominations 1, 5,
and 10 that changes money.
'''



def Change1(money):
    coins = 0

    while money > 0:
        
        if money>= 10:
            money -= 10
            coins +=1
        elif money >= 5:
            money -=5
            coins +=1
        else:
            money -=1
            coins +=1
    return coins



def Change2(money):

    return ((money//10) + ((money%10)//5) + (money%5))





def Change3(money):
    denominater = [10,5,1]
    number_coin = 0
    idx = 0
    largest_den = denominater[idx]
    while money>0:
        if money >= largest_den:
            money -= largest_den
            number_coin += 1
        else:
            idx +=1
            largest_den = denominater[idx]
            #print(f"index {idx} , denomination {largest_den}")
            
    return number_coin
        
        





if __name__ == "__main__":
    m = int(input())
    print(Change2(m))

