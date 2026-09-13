# Leetcode 645 : Set Mismatch
# Difficulty : Easy

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        for i in nums:
            if i in seen:
                dup=i
            seen.add(i)
        for i in range(1, len(nums) + 1):
            if i not in seen:
                missing = i
        return [dup, missing]