class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=len(nums)
        b=len(set(nums))
        print(a)
        print(b)
        if a==b:
            return False
        else:
            return True
            