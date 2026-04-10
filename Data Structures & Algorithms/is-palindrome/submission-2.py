class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        s=s.lower()
        while l<r:
            if not self.alNums(s[l]):
                l+=1
                continue
            if not self.alNums(s[r]):
                r-=1
                continue
                
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True

    def alNums(self, s:str):
        return (ord('a')<=ord(s)<=ord('z') or ord('0')<=ord(s)<=ord('9'))