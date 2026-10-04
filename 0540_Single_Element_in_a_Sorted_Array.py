# Leetcode 540 : Single Element in a Sorted Array
# Difficulty : Medium
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans=0
        for x in nums:
            ans^=x
        return ans