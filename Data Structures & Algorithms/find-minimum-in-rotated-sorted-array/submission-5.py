class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        mini =float("inf")
        if nums[l]<nums[r]:
            return nums[l]
        elif len(nums)==1:
            return nums[0]
        while l<=r:
            mid = (l+r)//2
            mini = min(nums[mid],mini)
            if nums[mid]>nums[r]:
                l=mid+1
            elif nums[mid]<nums[r]:
                r=mid-1
            else:
                return mini
        return mini
