class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        #key is n and value is index
        
        for i ,n in enumerate(nums):
            diff=target-n
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[n]=i
        return     
        
        