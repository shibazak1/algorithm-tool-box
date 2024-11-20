#celebration party statte that :
#if you have n children can you groupe this children into minimum number of group
#with constrain that no tow children with age gap more than 2 years


#it turn out that this problem is simuler to point cover by segemnt problem
#what is the minimum number of segemnt of leangth  needed to cover n point

def PointsCoverSorted(points):
    segments = []
    segment_left = points[0]

    for point in points:
        if point >= segment_left and point <= segment_left+2:
            continue
        else:
            segments.append((segment_left,segment_left+2))
            segment_left = point

    
    segments.append((segment_left,segment_left+2))
    segment_left = point

    return segments


#-------------------------------------------------------------


# this greedy algorithm make a segment from start form left most point to left most +2
# skip all the point in the same segment by increasing the left index varaible
# if the point not in the range make other segment and repeat
# the runing time is O(n) becouse we change the veraible left at etch step and the internal while also
# increase the vatiable left so it does not start over or repeate any thing to say it n^2 

def PointsCoverSorted2(points):
    #create an empty list 
    segments = []
    left  = 0 #assigning the index of first point as the left most point

    while left < len(points):
        #while there is uncovered point in the list
        x_left = points[left] # assagining the left coordinate of the segment 
        x_right = points[left]+2 # assaigning the right coordinate of the segment

        #makeing and appending the segemnt 
        segment = (x_left,x_right) 
        segments.append(segment)
        
        left += 1 # increasing the left to be the next index in the list 

        # after  we establish the segment we need to skip all the point that is in the range of the segment
        while left < len(points) and points[left] <= x_right:
            #so we cheaking etch time if the point sill in the range if true
            #incease the left index to point to the next index
            left += 1
    return segments
            
        
        


            

points = [2,4,5,6,7,8]
print(PointsCoverSorted(points))
    



