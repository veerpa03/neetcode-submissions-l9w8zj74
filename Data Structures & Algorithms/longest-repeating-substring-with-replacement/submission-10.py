class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l,r = 0,0

        maxfreq = 1
        res = 1
        while r<len(s):
            freq[s[l]] = freq.get(s[l],0)+1
            maxfreq = max(freq.values())
            while r-l+1<= k+maxfreq and r<len(s):
                r+=1
                if r>len(s)-1:
                    break
                freq[s[r]] = freq.get(s[r],0)+1
                maxfreq = max(freq.values())
            freq={}
            res = max(res,r-l)
            l+=1
            r=l

        return res