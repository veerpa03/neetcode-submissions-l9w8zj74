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
            if s[i] not in maps:
                if len(stack)==0 or maps[stack[-1]]!=s[i]:
                    return False
                else:
                    stack.pop()
            
        if  stack:
            return False
        
        return True
