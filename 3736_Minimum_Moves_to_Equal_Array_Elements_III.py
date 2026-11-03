# Leetcode 3736 : Minimum Moves to Equal Array Elements III
# Difficulty : Easy

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return len(nums)*max(nums)-sum(nums)