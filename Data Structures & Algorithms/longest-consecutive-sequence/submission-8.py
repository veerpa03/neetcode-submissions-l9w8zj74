class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lists = set(nums)
        longest = 0
        for num in  nums:
            if num-1 not in lists:
                lenght =1 
                while num+lenght in lists:
                    lenght+=1
                longest = max(lenght,longest)
        return longest
                    

        
