# Leetcode 27 : Remove Element
# Difficulty : 27

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)