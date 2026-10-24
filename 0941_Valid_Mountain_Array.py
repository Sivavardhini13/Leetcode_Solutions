# Leetcode 941 : Valid Mountain Array
# Difficulty : Easy

class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n=len(arr)
        i=0
        # climb up
        while i+1<n and arr[i]<arr[i+1]:
            i+=1
        # check peak
        if i==0 or i==n-1:
            return False
        # descend
        while i+1<n and arr[i]>arr[i+1]:
            i+=1
        # check if mountain
        return i==n-1