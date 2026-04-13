class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l,r = 0,0

        maxfreq = 1
        res = 1
        while r<len(s):
            freq[s[r]] = freq.get(s[r],0)+1
            maxfreq = max(freq.values())
            if r-l+1> k+maxfreq:
                freq[s[l]]-=1
                l+=1

            res = max(r-l+1,res)
            r+=1

        return res