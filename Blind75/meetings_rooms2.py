
#with two pointer approach
def minMeetingRoom(intervals):
     #Sort first index in the intervals
    start = sorted([i[0] for i in intervals])
    #Sort second index in the intervals 
    end = sorted([i[1] for i in intervals]) 
    #res variable to 0
    res = 0 
    #count variable to 0
    count = 0  
    
    s, e = 0, 0 
    #until s is less than interval length
    while s < len(intervals):   
        #if start value is less than end
        if start[s] < end[e]:   
            s += 1
            count += 1
        else: 
            #else doincrement e and decremnt count
            e += 1
            count -= 1
         #Compare the maximum between res and count and store it in res   
        res = max(res, count)   
    return res 

print(minMeetingRoom([(0,30),(5,10),(15,20)]))


#using minheap approach
from heapq import heappush, heappop

def minMeetingRoom(intervals):
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[0])
    rooms = []

    for interval in intervals:
        if rooms and interval[0] < rooms[0]:
            heappush(rooms, interval[1])
        else:
            heappop(rooms)
            heappush(rooms, interval[1])
    return len(rooms)

print(minMeetingRoom([[0,30],[5,10],[15,20]]))
