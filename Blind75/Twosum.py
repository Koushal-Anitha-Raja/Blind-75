class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        #key is n and value is index
        #iterate through the i and n values 
        for i ,n in enumerate(nums):
            #difference value is target minus n value
            diff=target-n
            #if difference in hashmap
            if diff in hashmap:
                #return the hashmap value od the diff var and current i th nums
                return [hashmap[diff],i]
            #assign hashmap of n to i
            hashmap[n]=i
            
        return     
        
        
