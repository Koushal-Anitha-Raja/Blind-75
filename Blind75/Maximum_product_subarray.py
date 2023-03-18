class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #curr min variable to nums[0]
        currentMinimum = nums[0]
        #curr max variable to nums[0]
        currentMaximum = nums[0]
        #global max var to nums[0]
        globalMaximum = nums[0]

        #start and end var to zero and one values respectively
        start = 0
        end = 1
        
        #iterate through the nums 
        for i in range(1,len(nums)):
            #Returning the maximum between currmax and curr min by having currmax value =currmin*current nums,currmax*nums[i],current nums and min between  currmin*current nums,currmax*nums[i],current nums
            currentMaximum,currentMinimum = max(currentMinimum * nums[i], currentMaximum * nums[i], nums[i]), min(currentMinimum * nums[i], currentMaximum * nums[i], nums[i])
              
                #if currmax is greater than currmin
            if (currentMaximum > globalMaximum):
                #assign globalmax to currentmax
                globalMaximum = currentMaximum
                #increment end value by one
                end=i+1
                #assign i value to j
                j=i
                #assign xurrentmax to contributor
                contributer = currentMaximum
                #iterate until j is greater than 0
                while j>=0:
                    #if nums[j] equal to zero
                    if nums[j]==0:
                        #assign start to j
                        start = j
                        #break the state
                        break
                    #or else if it is equal or lesser    
                    else:
                        if contributer == nums[j]:
                            start = j
                            #assign start to j and break
                            break
                            #contributor is contributor dived by nums[j]
                        contributer = contributer/nums[j]
                    #decrement j by one
                    j-=1


    #assign prod to one
        prod = 1
        #iterate through the nums from start to end
        for num in nums[start: end]:
            #prod =prod *num
            prod *=num
            print(num)
#return the prod
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



   

           
        
