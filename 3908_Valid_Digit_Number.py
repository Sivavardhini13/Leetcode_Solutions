# Leetcode 3908 : Valid Digit Number
# Difficulty : Easy

class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        return str(x) in str(n) and str(n)[0]!=str(x)