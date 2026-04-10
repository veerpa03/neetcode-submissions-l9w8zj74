class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        dups = set()
        l=0
        for r in range(len(s)):
            while s[r] in dups:
                dups.remove(s[l])
                l+=1
            dups.add(s[r])
            length = max(length,r-l+1)
        return length

            
