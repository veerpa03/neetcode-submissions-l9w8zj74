class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res = [1]*n
        left = [1]*n
        right = [1]*n
        product = 1
        left[0]=1
        right[n-1]=1
        for i in range(1,len(nums)):
            left[i]=left[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]

        for i in range(n):
            res[i]=left[i]*right[i]
        return res