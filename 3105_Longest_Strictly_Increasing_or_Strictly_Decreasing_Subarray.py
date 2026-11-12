# Leetcode 3105 : Longest Strictly Increasing or Strictly Decreasing Subarray
# Difficulty : Easy

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec, res = 1, 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1
                res = max(res, inc)
            elif nums[i] < nums[i-1]:
                dec += 1
                inc = 1
                res = max(res, dec)
            elif nums[i] == nums[i-1]:
                inc = 1
                dec = 1
        return res