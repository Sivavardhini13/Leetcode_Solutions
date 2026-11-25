# Leetcode 2413 : Smallest Even Multiple
# Difficulty : Easy

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n * 2