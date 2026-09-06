# Leetcode 2733 : Neither Minimum nor Maximum
# Difficulty : Easy

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums=sorted(nums)
        for i in range(len(nums)):
            if len(nums)<=2:
                return -1
            else:
                return nums[1]