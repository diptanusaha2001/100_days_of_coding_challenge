class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        l=1
        r=n-2
        while l<r:
            m=(l+r)//2
            if arr[m-1] < arr[m] and arr[m]>arr[m+1]: 
                return m
            elif arr[m]<arr[m+1]:
                l=m+1 
            else:
                r=m-1
        return l
