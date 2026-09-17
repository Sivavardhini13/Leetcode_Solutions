# Leetcode 198 : House Robber
# Difficulty : Medium

class Solution:
    def rob(self, nums: list[int]) -> int:
        prev=0
        curr=0
        for i in nums:
            new=max(curr, prev+i)
            prev=curr
            curr=new
        return curr