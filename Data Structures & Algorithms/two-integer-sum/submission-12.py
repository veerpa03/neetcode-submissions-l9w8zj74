class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        look = {}
        for i in range(len(nums)):
            look[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in look and i!=look[diff]:
                return [i,look[diff]]