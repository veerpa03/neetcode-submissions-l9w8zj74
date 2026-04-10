class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]]=count.get(nums[i],0)+1
        freq = [[] for _ in range(len(nums)+1)]
        for key, value in count.items():
            freq[value].append(key)
        store = []
        for i in range(len(nums), -1,-1):
            for j in range(len(freq[i])):
                store.append(freq[i][j])
                if len(store)==k:
                    return store
                