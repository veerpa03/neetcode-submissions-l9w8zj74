class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_S, count_T ={}, {}
        for items in s:
            if items in count_S:
                count_S[items]+=1;
            else:
                count_S[items]=1
        for items in t:
            if items in count_T:
                count_T[items]+=1;
            else:
                count_T[items]=1
        if count_S==count_T:
            return True
        else:
            return False