# Leetcode 2716 : Minimize String Length
# Difficulty : Easy

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))