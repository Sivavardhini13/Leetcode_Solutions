# Leetcode 215 : Kth Largest Element in an Array
# Difficulty : Easy

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        return nums[-k]