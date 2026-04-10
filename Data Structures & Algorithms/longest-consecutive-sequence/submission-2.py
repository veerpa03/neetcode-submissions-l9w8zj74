class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxx = 0
        for n in num_set:
            count=1
            curr=n
            while curr+1 in num_set:
                count+=1
                curr+=1
            maxx = max(maxx, count)
        return maxx