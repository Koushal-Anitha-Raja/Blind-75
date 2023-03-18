class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #d var for lenght of nums
        d=len(nums)-1

        #iterate through the nums from one before element in reverse order
        for i in range(len(nums)-2,-1,-1):
            #if current nums value plus i is greater than d 
            if nums[i]+i>=d:
                #assign d to i
                d=i
        #if d value os zero return true
        if d==0:
            return True
        #else return false
        else:
            return False
