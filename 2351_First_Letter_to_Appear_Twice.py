# Leetcode 2351 : First Letter to Appear Twice
# Difficulty : Easy

class Solution:
    def repeatedCharacter(self, s: str) -> str:
         seen=set()
         for ch in s:
             if ch in seen:
                 return ch
             seen.add(ch)