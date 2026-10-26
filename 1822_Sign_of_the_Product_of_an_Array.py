# Leetcode 1822 : Sign of the Product of an Array
# Difficulty: Easy

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        res=1
        for num in nums:
            res*=num
        if res>0:
            return 1
        elif res==0:
            return 0
        else:
            return -1