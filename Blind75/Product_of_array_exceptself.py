#TC:0(2n)
#SC:0(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
    #declaring a resultant array to 1 as product is calculated
        result=[1]
    
    #iterate the array in single pass
        for i in range (1,len(nums)):
            #this will give u the prefix sum
            result.append(nums[i-1]*result[-1])
        
        #this is for storing the suffix running product  value
        suffixproduct=1
        
        #reverse iterating the resultant array to find the suffix product value
        #last element is going to be 1 so loop from (-2)
        for i in range (len(result)-2,-1,-1):
            #adding the suffix product to resultant array
            result[i]=result[i]*nums[i+1] *suffixproduct
            suffixproduct=suffixproduct*nums[i+1]
        
        #returning the resultant array
        return result
            
            
        
