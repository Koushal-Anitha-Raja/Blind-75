#TC:0(n)
#SC:0(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #lenght of the a
        a=len(nums)
        #add the b value to hashset to remove duplicate
        b=len(set(nums))
        print(a)
        print(b)
        #if it has duplicate return false
        if a==b:
            return False
        #If it does not have duplicates return true
        else:
            return True
            
