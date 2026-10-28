# Leetcode 2390 : Removing Stars From a String
# Difficulty : Medium 

class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for c in s:
            if c=="*":
                stack and stack.pop()
            else:
                stack.append(c)
        return "".join(stack)