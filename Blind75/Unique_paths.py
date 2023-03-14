class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # previous row with 1 to the length of n
        prevrow = [1] *n 
         #if m is one 
        if m == 1:
            return 1
        #iterate theough the m values
        for i in range(m-1):
            # creating the row of 1 with the length of n
            currRow = [1]*n 
            #iterate in rverse from n-2 to the -1 index position
            for j in range(n-2,-1,-1):
                #adding currrow j+1 to prevrow j values to the currrow
                currRow[j] = currRow[j+1] + prevrow[j] 
            #assig prevrow to currrow
            prevrow = currRow
#return first index of currrow
        return currRow[0]
        