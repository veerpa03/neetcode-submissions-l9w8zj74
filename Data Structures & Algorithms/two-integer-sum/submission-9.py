class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]]=i
        diff = 0
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in count and i!=count[diff]:
                return [i,count[diff]]
        
