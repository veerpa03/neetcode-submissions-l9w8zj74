class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n
        left = 1
        # for i in range(2,n+1):
        #     right[n-i] = right[n-i+1] * nums[n-i+1]


        # for i in range(1, n):
        #     left[i]=left[i-1]*nums[i-1]

        for i in range(n):
            output[i] = left
            left *= nums[i]
        right = 1

        for i in range(n-1,-1,-1):
            output[i] = output[i]*right
            right = right*nums[i] 
        return output
        