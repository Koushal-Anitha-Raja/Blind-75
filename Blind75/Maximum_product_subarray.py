class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        currentMinimum = nums[0]
        currentMaximum = nums[0]
        globalMaximum = nums[0]

        start = 0
        end = 1
        
        for i in range(1,len(nums)):
            currentMaximum,currentMinimum = max(currentMinimum * nums[i], currentMaximum * nums[i], nums[i]), min(currentMinimum * nums[i], currentMaximum * nums[i], nums[i])
              
            if (currentMaximum > globalMaximum):
                globalMaximum = currentMaximum
                end=i+1
                j=i
                contributer = currentMaximum
                while j>=0:
                    if nums[j]==0:
                        start = j
                        break
                    else:
                        if contributer == nums[j]:
                            start = j
                            break
                        contributer = contributer/nums[j]
                    j-=1


    
        prod = 1
        for num in nums[start: end]:
            prod *=num
            print(num)

        return prod
     

       # currentMaximum = nums[0]
        # currentMinimum = nums[0]
        # globalMaximum = nums[0]
        
        # for i in range(1, len(nums)):
        #     tempmax = currentMaximum * nums[i]
        #     tempmin = currentMinimum * nums[i]
        #     currentMaximum = max(nums[i], max(tempmax, tempmin))
        #     currentMinimum = min(nums[i], min(tempmax, tempmin))
        #     globalMaximum = max(globalMaximum, currentMaximum)
        
        # return globalMaximum



   

           
        
