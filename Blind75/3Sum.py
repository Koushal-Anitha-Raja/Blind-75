#using hashset: TC--> o(n^2),Sc:o(n)
#using binary search :TC-->o(n^2)(logn) Sc:o(c)
#using two pointers
#Time complexity:o(n^2)
#space complexity:o(C)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #the kength of the nums array
        n = len(nums)-1
        #sort the array
        nums.sort()
        #resultant array
        result = []

        #iterate through the array nums
        for i in range(n-1):
            #checking if the i is greater than zero then nums and next to nums are equal 
            if i>=1 and nums[i]==nums[i-1]:
                #then continue
                continue

            #assign j as next to i
            j = i+1
            #assign k to n
            k = n
            #set the target value
            target = 0 - nums[i]

            #iterate until j is less than k
            while j<k:
                #if target is equal to nums[j] and k
                if nums[j] + nums[k] == target:
                    #append it to resultant array
                    result.append([nums[i],nums[j],nums[k]])
                    
                    
                    #iterate until j is less than k and nums[j] and j +1 is equal
                    while j<k and nums[j] == nums[j+1]:
                        #increment j to one
                        j+=1

                    #iterate until j is less than k and nums[k] is equal to k-1
                    while j<k and nums[k] == nums[k-1]:
                        #increment k to one 
                        k-=1

                    #go to the next new element
                    j+=1
                    k-=1

                #if the target is not equal to nums of j and k
                else:
                    #if target is less than total of j and k 
                    if target < (nums[j]+nums[k]):
                        #decrement k by one
                        k-=1
                        #if not increment j by one
                    else:
                        j+=1

        #returning the resultanr array
        return result
        
