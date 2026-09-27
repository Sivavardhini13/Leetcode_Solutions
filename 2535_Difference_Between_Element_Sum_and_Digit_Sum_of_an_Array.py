# Leetcode 2535 : Difference Between Element Sum and Digit Sum of an Array
# Difficulty : Easy

class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        digit_sum=0
        for n in nums:
            while n>0:
                digit_sum+=n%10
                n//=10
        return abs(sum(nums)-digit_sum)