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
            if s[r] in seen:
                
                seen.clear()
                l+=1
                r=l
                seen.add(s[l])
                
            else:
                seen.add(s[r])
            maxi = max(maxi,len(seen))

            r+=1
        return maxi

