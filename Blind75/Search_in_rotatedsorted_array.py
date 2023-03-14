class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #assigning low value to zero
        l=0
        #assigning high value to last value (here one less then length as index starts from 0)
        h=len(nums)-1
        
        
        #continue until low is less than or equal high
        while l<=h:
            #finding the mid value with integer overflow check
            mid=l+(h-l)//2
            
            #if mid value is the target     
            if (nums[mid]==target):
                return mid
                
            #if left is sorted 
            if (nums[l]<=nums[mid]):
                #if it lies in the range between low and minimum
                if (nums[l]<=target and target<nums[mid]):
                    h=mid-1
                    
                    #move the high to mid -1
                else:
                    #or else move the low to mid +1
                    l=mid+1
                
            else:
                #if the target lies in the range between mid and high
                if (nums[mid]<target and target<=nums[h]):
                    #move the hight to mid +1
                    l=mid+1
                else:
                    #move the low to mid -1
                    h=mid-1
              #orelse return -1 if not found the target     
        return -1
                
            