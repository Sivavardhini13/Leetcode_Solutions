# Leetcode 3866 : First Unique Even Element
# Difficulty : Easy

from collections import Counter
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        ctr=Counter(nums)
        for n, c in ctr.items():
            if n%2==0 and c==1:
                return n
        return -1