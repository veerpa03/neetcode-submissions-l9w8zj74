class Solution:
    def isPalindrome(self, s: str) -> bool:
            l,r = 0,len(s)-1
            s= s.lower()
            while l<r:
                while s[l].isalnum()==False and l<r:
                    l+=1
                while s[r].isalnum()==False and l<r:
                    r-=1
                while s[l].isalnum() and s[r].isalnum() and l<r:
                    if s[l]==s[r]:                 
                        l+=1
                        r-=1
                    else:
                        return False
                
            return True