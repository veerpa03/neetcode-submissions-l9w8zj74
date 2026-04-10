class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res+=str(len(strs[i])) + '#' + strs[i]
        return res        

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            lenght=int(s[i:j])
            j+=1
            res.append(s[j:lenght+j])
            i=lenght+j
        return res