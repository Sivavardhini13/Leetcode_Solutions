# Leetcode 162 : Find Peak Element
# Difficulty : Medium

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        return (nums.index(max(nums)))