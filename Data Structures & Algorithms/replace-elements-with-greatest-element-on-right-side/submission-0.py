class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = float("-inf")
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                maxi = max(maxi ,arr[j])
            arr[i] = maxi
            maxi = float("-inf")
        
        arr[-1]=-1
        return arr
