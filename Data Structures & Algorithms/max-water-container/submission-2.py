class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        for i in range(len(heights)):
            j=i+1
            while j<len(heights):
                area = (j-i) * min(heights[i],heights[j])
                maxi = max(area,maxi)
                j+=1
        return maxi