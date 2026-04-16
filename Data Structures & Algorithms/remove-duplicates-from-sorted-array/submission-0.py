class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0 
        p2 = 1
        k=1
        while p2<len(nums):
            while  p2<len(nums) and  nums[p1] == nums[p2] :
                p2+=1
            
            if p2>=len(nums):
                return k
            nums[k] = nums[p2]
            k+=1
            p1=p2
            p2+=1

        return k
        
