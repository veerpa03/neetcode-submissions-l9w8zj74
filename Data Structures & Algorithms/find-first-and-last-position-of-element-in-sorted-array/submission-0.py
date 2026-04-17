class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        

        while l<=r:
            mid = (l+r)//2

            if nums[mid]==target:
                start = mid
                end   = mid
                while start >=0 and target == nums[start]:
                    start-=1
                
                while end<len(nums) and target == nums[end]:
                    end+=1
                return [start+1,end-1]
            elif target > nums[mid]:
                l=mid+1
            else:
                r = mid-1
        return [-1,-1]