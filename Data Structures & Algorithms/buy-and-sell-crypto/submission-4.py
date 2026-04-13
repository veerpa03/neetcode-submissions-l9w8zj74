class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = float("-inf")

        i = 0
        j=i+1
        while i<len(prices) and j<len(prices):
            if prices[j]-prices[i] <0:
                i+=1
                j=i+1
            else:
                diff = prices[j]-prices[i]
                maxi = max(maxi,diff)
                j+=1
        if maxi<0:
            return 0
        else:
            return maxi