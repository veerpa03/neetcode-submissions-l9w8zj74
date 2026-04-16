class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ""
        for i in range(len(strs[0])):
            j=0
            ch = strs[j][i]

            while j<len(strs):
                if i >= len(strs[j]):
                    return string
                if ch == strs[j][i]:
                    j+=1
                else:
                    return string
                    
            string +=ch
        return string