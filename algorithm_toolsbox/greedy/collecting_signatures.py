
'''
Covering Segments by Points Problem

Find the minimum number of points needed to cover all given segments on a line.

Input: A sequence of n segments [l1 , r1 ], . . . , [ln , rn ] on a line.

Output: A set of points of minimum size such that each segment
[li , ri ] contains a point, i.e., there exists a point x from this set such that
li ≤ x ≤ ri .
'''

#-----------------------------------------------------------------------------------

def MinimumNumberOfPoint(segments):


    points = []
    first_ending_seg = segments[0]

    while segments:
        print("enter while")
        
        for i in range(1,len(segments)):
            if segments[i][1]<= first_ending_seg[1]:
                first_ending_seg = segments[i]


        curr_point = first_ending_seg[1]
        points.append(curr_point)


        for seg in segments:
            print("segments = ",segments)
            print("seg = ",seg)
            if seg[0]<= curr_point and seg[1]>=curr_point:
                segments.remove(seg)
    return points
#----------------------------------------------------------------------------------
#create a new type (segment)
from collections import namedtuple
import sys
Segment = namedtuple("segment","left right")

def IsCovered(segment,point):
    return segment.left<=point<=segment.right

def SegmentCovered(segments):
    points = []

    while len(segments)>0:

        r = min([seg.right for seg in segments ])

        points.append(r)
        segments = [seg for seg in segments if not IsCovered(seg,r)]

    return points
#-------------------------------------------------------------------------------------

Segment = namedtuple("segment","left right")

def SegmentCovered2(segments):

    
    points = []
    #if we sorte the list according to it right corrdinate
    #so the 1st ending segment it will be in order 
    segments = sorted(segments,key = lembda s: s.right)

    r = -1
    #if we know that the segment inorder so pick r for 1st ending segment
    # only if this segment not coverd by this point 
    for seg in segments:
        if r<seg.left:
            r = seg.right
            points.append(r)
    return points


        
    
    



#----------------------------------------------------------------------------------
"""
if __name__ == '__main__':

    segments = []
    n = int(input("enter n: "))
    
    for i in range(n):
        seg = list(map(int,input().split()))
        segments.append(seg)


    points = MinimumNumberOfPoint(segments)
    print(len(points),points)
 
"""

if __name__ =="__main__":

    n, *data = map(int,sys.stdin.read().split())
    segments = list(map(lambda x:Segment(x[0],x[1]),
                        zip(data[::2],data[1::2])))

    points = SegmentCovered(segments)
    print(len(points),points)

    
