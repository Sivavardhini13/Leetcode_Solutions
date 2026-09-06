# Leetcode 414 : Third Maximum Number
# Difficulty : Easy

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        nums=sorted(nums)
        for i in range(len(nums)):
            if len(nums)>=3:
                return nums[-3]
            else:
                return max(nums)