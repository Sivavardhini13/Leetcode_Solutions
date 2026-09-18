# Leetcode 287 : Find the Duplicate Number
# Difficulty : Medium

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        s = set()

        for i in nums:
            if i in s:
                return i
            s.add(i)