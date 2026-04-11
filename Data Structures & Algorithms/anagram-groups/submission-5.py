class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for strings in strs:
            alphabets = [0]*26
            for ch in strings:
                num = 97-ord(ch)
                alphabets[num-1]+=1
            key = tuple(alphabets)
            anagram[key].append(strings)
        
        res = []

        for i in anagram.values():
            res.append(i)
        return res

        