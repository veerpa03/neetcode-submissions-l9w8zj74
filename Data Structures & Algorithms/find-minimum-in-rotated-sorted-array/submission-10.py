class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = float('inf')
        l,r = 0, len(nums)-1

        while l<r:
            mid = (l+r)//2

            if nums[mid]> nums[r]:
                l=mid+1
                mini = min(nums[r],mini)
            elif nums[mid]<nums[r]:
                r= mid
            
        return nums[r]
