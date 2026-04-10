class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for ch in strs:
            lists = [0]*26
            for i in ch:
                lists[ord(i)-97]+=1
            if tuple(lists) not in d:
                d[tuple(lists)]=[]
            d[tuple(lists)].append(ch)
        return list(d.values())