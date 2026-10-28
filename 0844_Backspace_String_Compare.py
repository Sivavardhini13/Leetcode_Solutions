# Leetcode 844 : Backspace String Compare
# Difficulty : Easy

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove_ch(s):
            stack=[]
            for ch in s:
                if ch=="#":
                    stack and stack.pop()
                elif ch!="#":
                    stack.append(ch)
            return stack
        return remove_ch(s)==remove_ch(t)