# Leetcode 2149 : Rearrange Array Elements by Sign
# Difficulty : Medium

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        res=[0]*len(nums)
        p,n=0,1
        for i in nums:
            if i>0:
                res[p]=i
                p+=2
            else:
                res[n]=i
                n+=2
        return res