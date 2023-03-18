class Solution:
    def rob(self, nums: List[int]) -> int:
        #if the list has only one element return it 
        if len(nums)==1:
            return nums[0]
         #run the loop by reomving first index and also run it again without last index
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    

    def helper(self,nums):
        rob1=0
        #first index
        rob2=0
        #second index
        #iterate through the nums list
        for i in range(len(nums)):
            #store the result as max between rob1 plus current nums and rob 2
            result=max(rob1+nums[i],rob2)
            #assign rob1 to rob2
            rob1=rob2
            #assign rob2 to result
            rob2=result
        #return the result
        return result
