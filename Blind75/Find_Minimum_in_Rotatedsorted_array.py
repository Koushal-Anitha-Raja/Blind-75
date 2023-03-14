class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #assigning low value to zero
        l=0
        #assigning high value to last value (here one less then length as index starts from 0)
        h=len(nums)-1
        
        #if the array is fully sorted
        if nums[l]<=nums[h]:
            return nums[l]
         
        #continue until low is less than or equal high
        while l<=h:
            
            #finding the mid value with integer overflow check
            mid=l+(h-l)//2
            
            #if the middle element is the peak the next dip in the graph is the minimum element
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            
            #or else if left side is sorted
            elif nums[l]<=nums[mid]:
                l=mid+1
            
            #if right side is sorted
            else:
                h=mid-1
                
        return          
            
            
            
        