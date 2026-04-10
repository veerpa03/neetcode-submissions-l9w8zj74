class Solution:
    def isValid(self, s: str) -> bool:
        bracet = {"(":")", "{":"}", "[":"]"}
        stack = []
        for i in s:
            if i in bracet:
                stack.append(i)
            else:
                if len(stack)>0 and i==bracet[stack[-1]] :
                    stack.pop()
                else:
                    return False
        return len(stack)==0
            
