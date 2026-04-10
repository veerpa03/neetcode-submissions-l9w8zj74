class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = {}
        n=len(nums)
        for i in nums:
            major[i]=major.get(i,0)+1
        
        for i in major:
            if major[i]>n/2:
                return i
