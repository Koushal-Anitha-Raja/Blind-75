#TC:0(n*n)
#SC:0(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #TC:0(nlogn)
    #     array = [nums[0]]
    #     for i in range (1, len(nums)):

    #         if nums[i]<=array[-1]:
    #             j=self.binary_search(array,nums[i])
    #             array[j]=nums[i]

    #         else:
    #             array.append(nums[i])
                
    #     return len(array)

    # def binary_search(self,nums,target):
    #         l = 0
    #         h = len(nums)-1
    #         while l <= h:
    #             mid = l +(h-l)//2
    #             if nums[mid] == target:
    #                 return mid
    #             elif nums[mid] < target:
    #                 l = mid + 1
    #             else:
    #                 h = mid-1
    #         return l    
            
            
    
     

        n = len(nums)
        dp = [1]*n
        dp2=[[] for i in range(n)]

        for i in range(n): 
            dp2[i] = [nums[i]]
            for j in range(i):
                if nums[i] > nums[j]: 
                    if dp[j]+1 > dp[i]: 
                        dp[i] = dp[j]+1 
                        dp2[i] = dp2[j] + [nums[i]]
        #print(len(dp2)) 
        for i in range (len(dp2)):
            if len(dp2[i])==max(dp):
                print(dp2[i])

                   
        #print(dp2)
                

    
        return max(dp)

        #------------------------
        
