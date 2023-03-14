class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)<3:
            return max(nums)
        
        #using two variables
        var1=nums[0]
        var2=max(nums[0],nums[1])

        for i in range(2,len(nums)):
            var3 = max(nums[i] + var1, var2)
            var1=var2
            var2=var3
        
        return var3
        