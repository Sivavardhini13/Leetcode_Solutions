# Leetcode 88 : Merge Sorted Array
# Difficulty : Easy

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ls=nums1[:m]+nums2[:n]
        nums1[:]=ls
        nums1.sort()
        return nums1
