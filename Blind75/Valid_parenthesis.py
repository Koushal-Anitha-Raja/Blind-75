class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2!=0:
            return False

        hashmap= { '}':'{', ']':'[', ')':'('}
        stack = []

        for ch in s:
            if ch in hashmap:
                if stack and stack[-1]==hashmap[ch]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(ch)

        return len(stack)==0

        