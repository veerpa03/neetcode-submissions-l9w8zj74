class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        maxi = arr[-1]
        for i in range(len(arr)-1,0,-1):
            store = arr[i-1]
            arr[i-1] = maxi
            maxi = max(maxi,store)
        arr[-1]=-1


        return arr

