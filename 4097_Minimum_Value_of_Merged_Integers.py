# Leetcode 4097 : Minimum Value of Merged Integers
# Difficulty : Easy

class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        ans=float("inf")
        for i in range(0,len(nums),2):
            merged=int(str(nums[i])+str(nums[i+1]))
            ans=min(ans,merged)
        return ans