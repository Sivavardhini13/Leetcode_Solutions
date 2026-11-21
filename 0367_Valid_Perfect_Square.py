# Leetcode 367 : Valid Perfect Square
# Difficulty : Easy

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Babylonian Method
        x = num
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num