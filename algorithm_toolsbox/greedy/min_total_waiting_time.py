
#minimum total waiting of pataint in que




def MinTotalWaitingTime(t,n):

    mwt = 0
    for i in range(n):
        for j in range(i+1,n):
            if t[j] <= t[i]:
                t[i],t[j] = t[j],t[i]
        
        mwt +=(n-(i+1))*t[i]
                
    return mwt


#-------------------------------------------------------------

def MinTotalWaitingTime2(t,n):
    treated = [0]*n
    mwt = 0

    for i in range(n):
        min_time = 100
        min_indx = 0
        for j in range(n):
            if treated[j] == 0 and t[j] < min_time:
                min_time = t[j]
                min_indx = j

        print(t[min_indx])
        wt  =  (n-(i+1)) * min_time
        mwt += wt
        treated[min_indx] = 1
    
        
    return mwt





pataints = [15,20,10] 
print(MinTotalWaitingTime(pataints,len(pataints)))

            
        

