#TC:0(n)
#SC:0(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        #if the length of the nums is only two return max between then
        

        if len(nums)<3:
            return max(nums)
        
        
        #using two variables
        var1=nums[0]
        #assigning var 2 as max between first and second house
        var2=max(nums[0],nums[1])
       
        #iterate through the loop until end from 2 nd index as we already checked for the first two
        for i in range(2,len(nums)):
            #assign a var3 and give max between current nums plus var1 or var2
            var3 = max(nums[i] + var1, var2)
            #assign var1 to var2
            var1=var2
            #assign var2 to var3
            var2=var3
        #return the var 3 which hold the overall robbed value
        return var3
        
