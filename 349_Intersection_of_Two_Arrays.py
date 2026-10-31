# Leetcode 349 : Intersection of Two Arrays
# Difficulty : Easy

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))