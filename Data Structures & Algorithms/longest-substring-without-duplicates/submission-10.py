class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 1
        seen = set()
        l=0
        r=1
        if not s:
            return 0
        seen.add(s[l])
        while r<len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
                
            else:
                seen.add(s[r])
            maxi = max(maxi,len(seen))

            r+=1
        return maxi

