# Leetcode 88 : Merge Sorted Array
# Difficulty : Easy

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k=len(nums1)-1
        i=m-1
        j=n-1
        while i>=0 and j>=0:
            v1, v2=nums1[i], nums2[j]
            if v1>v2:
                nums1[k]=v1
                i-=1
            else:
                nums1[k]=v2
                j-=1
            k-=1
        while j>=0:
           nums1[k]=nums2[j] 
           j-=1
           k-=1