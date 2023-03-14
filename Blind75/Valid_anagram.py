class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        bucket=[0]*26

        for ch in s:
            bucket[ord(ch)-ord("a")]+=1
        for ch in t:
            bucket[ord(ch)-ord("a")]-=1
            if bucket[ord(ch)-ord('a')] < 0:
                return False
        
        return True



         

        

        