class Solution:
    def isValid(self, s: str) -> bool:
        maps = {"[":"]", "{":"}","(":")"}
        n=len(s)

        stack = []
        if len(s)==0 or len(s)==1:
            return False

        for i in range(len(s)):
            if s[i] in maps:
                stack.append(s[i])
            else:
                if len(stack)==0 or maps[stack[-1]]!=s[i]:
                    return False
                else:
                    stack.pop()
        
        return not stack
