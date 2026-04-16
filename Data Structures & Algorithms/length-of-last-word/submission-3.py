class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0 
        if len(s)==0:
            return length

        for i in range(len(s)-1, -1,-1):
            j=i
            while j>0 and s[j].isalpha():
                j-=1
                length+=1
            if length>=1:
                return length
        return length+1