class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency  = {}
        for i in nums:
            frequency[i]=frequency.get(i,0)+1

        count = [[] for i in range(len(nums))]
        for i in frequency:
            count[frequency[i]-1].append(i)
        res = []
        for i in range(len(count)-1,-1,-1):
            for j in count[i]:
                if k==len(res):
                    return res
                res.append(j)
        return res