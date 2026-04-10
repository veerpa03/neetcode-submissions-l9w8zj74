class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n
        left = [1]*n
        right = [1]*n

        for i in range(n-1):
            for j in range(i+1, n):
                right[i]*=nums[j]
        for i in range(1, n):
            for j in range(i):
                left[i]*=nums[j]
        for i in range(n):
            output[i] = left[i]*right[i]
        return output
        