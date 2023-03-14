class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    


    def helper(self,nums):
        rob1=0
        #first index
        rob2=0
        #second index
        for i in range(len(nums)):
            result=max(rob1+nums[i],rob2)
            rob1=rob2
            rob2=result8
        return result