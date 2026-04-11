class Solution:
    def maxArea(self, heights: List[int]) -> int:
        w = 0
        h = 0
        maxi = 0

        l,r = 0,len(heights)-1
        while l<=r:
            w = r-l
            h = min(heights[l],heights[r])
            area = w*h
            maxi = max(maxi,area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxi
