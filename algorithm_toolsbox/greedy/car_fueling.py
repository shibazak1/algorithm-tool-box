

'''
Car Fueling Problem

Compute the minimum number of gas tank refills to get from one city to another.

Input: Integers d and m, as well as a sequence of integers stop1 < stop2 < · · · < stopn .

Output: The minimum number of refills to get from one city to an-other
if a car can travel at most m miles on a full tank.
The distance between the cities is d miles and there are gas stations at distances stop1 , stop2 , . . . , stopn along the way.

We assume that a car starts with
a full tank.
'''

#-----------------------------------------------------------------------------
# 0 200 375 550 750 900
# 0,1,2,5,9,10

import sys

def NumberOfRfueling(d,m,stations):
    
    stations  = [0] + stations +[d]
    position = 0
    refill = 0
    while stations[position] + m < d:
        for i in range(position,len(stations)):
            if stations[i+1] - stations[position] > m:
                if stations[position] == stations[i]:
                    return -1
                
                position = i
                refill +=1
                break
                
            
    return refill
    
#--------------------------------------------------------------------

# 0 200 375 550 750 900

# 0,1,2,5,9,10

def compute_min_refills(distance, tank, stops):
    stops = [0] + stops +[distance]
    num_refill , curr_station = 0,0

    while curr_station <= len(stops)-2:
        last_station  = curr_station
        while curr_station <= len(stops)-2 and stops[curr_station+1] - stops[last_station]:
            curr_station +=1

        if curr_station == last_station:
            return -1
        if curr_station <= len(stops)-2:
            num_refill +=1
            
    return num_refill
#--------------------------------------------------------------------
# 200 375 550 750
# 1,2,5,9
def refill(location,distance,tank,stops):

    if location + tank >= distance:
        return 0

    if not stops or stops[0] - location > tank:
        return float('inf')

    last_stop = location
    
    while stops or stops[0] - location <= tank:
        last_stop = stops[0]
        stops.pop(0)

    return 1+refill(last_station,distance,stank,stops)







#--------------------------------------------------------------------
data  = list(map(int,sys.stdin.read().split()))                

d = data[0]
m = data[1]
stations = data[2:]


print(NumberOfRfueling(d,m,stations))
            
            
            
