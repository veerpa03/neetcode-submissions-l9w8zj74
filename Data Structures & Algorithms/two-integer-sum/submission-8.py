class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sum_dict = {}
        for i in range(len(nums)):
            sum_dict[nums[i]]=i
        
        for i in range(len(nums)):
            sums=target-nums[i]
            if sums in sum_dict and (i!=sum_dict[sums]):
                return [i,sum_dict[sums]]