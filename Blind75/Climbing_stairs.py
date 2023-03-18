class Solution:
    def climbStairs(self, n: int) -> int:
        #assign two variables as initial value one
        one,two=1,1
        #iterate through the n value
        for i in range (n-1):
            #assigning temp to one for not losing track of the one
            temp=one
            #adding at each step to one as one plus two
            one=one+two
            #then assign two to temp variuable
            two = temp
        #finally return the one 
        return one    
            
            
            
        
