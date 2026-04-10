class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d= defaultdict(list)
        for words in strs:
            count = [0]*26
            for ch in words:
                count[ord(ch)-ord('a')] +=1
            d[tuple(count)].append(words)
        return list(d.values())            