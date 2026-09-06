# Leetcode 136 : Single Number
# Difficulty : Easy

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans
