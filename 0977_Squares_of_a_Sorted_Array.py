# Leetcode 977 : Squares of a Sorted Array
# Difficulty : Easy

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([i**2 for i in nums])