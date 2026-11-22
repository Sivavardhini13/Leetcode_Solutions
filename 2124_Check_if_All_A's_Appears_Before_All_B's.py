# Leetcode 2124 : Check if All A's Appears Before All B's
# Difficulty : Easy

class Solution:
    def checkString(self, s: str) -> bool:
        return "ba" not in s