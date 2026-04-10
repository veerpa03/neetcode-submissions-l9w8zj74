class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        # if len(sets)==0:
        #     return 0
        maxi=0
        for n in sets:
            current=n
            count=1
            while (current+1) in sets:
                current+=1
                count+=1
            maxi =  max(maxi, count)
        
        return maxi