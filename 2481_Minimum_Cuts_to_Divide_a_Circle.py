# Leetcode 2481 : Minimum Cuts to Divide a Circle
# Diffficulty : Easy

class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1: return 0
        return n if n % 2 != 0 else n // 2