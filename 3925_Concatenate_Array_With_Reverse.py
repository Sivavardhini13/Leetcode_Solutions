# Leetcode 3925 : Concatenate Array With Reverse
# Difficulty : Easy

class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums+nums[::-1]