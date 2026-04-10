class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = {}, {}
        for i in range(0,len(s)):
            count_s[s[i]] = count_s.get(s[i],0)+1
             
        for i in range(0,len(t)):
            count_t[t[i]] = count_t.get(t[i],0)+1
        return count_s==count_t
