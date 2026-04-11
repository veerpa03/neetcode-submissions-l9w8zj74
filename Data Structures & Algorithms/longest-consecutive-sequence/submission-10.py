class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        sets = set(nums)
        maxi = 1

        for i in sets:
            if i-1 not in sets:
                j=i
                lenght = 1
                while j+1 in sets:
                    lenght+=1
                    j+=1
                maxi = max(maxi,lenght)

        return maxi
