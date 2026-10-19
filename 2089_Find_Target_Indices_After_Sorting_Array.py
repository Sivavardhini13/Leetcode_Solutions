# Leetcode 2089 : Find Target Indices After Sorting Array
# Difficulty : Easy

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        return [i for i in range(len(nums)) if nums[i]==target]