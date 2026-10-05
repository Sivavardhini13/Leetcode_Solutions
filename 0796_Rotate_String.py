# Leetcode 796 : Rotate String
# Difficulty : Easy

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        return goal in s+s