class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set(nums)
        n1 = len(nums)
        n2 = len(myset)
        if n1==n2:
            return False
        else:
            return True

