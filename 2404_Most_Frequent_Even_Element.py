# Leetcode 2404 : Most Frequent Even Element
# Difficulty : Easy

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        ans={}
        for i in nums:
            if i in ans:
                ans[i]+=1
            else:
                ans[i]=1
        freq=0
        res=-1
        for nums, c in ans.items():
            if nums%2==0:
                if c>freq or (c==freq and nums<res):
                    freq=c
                    res=nums
        return res