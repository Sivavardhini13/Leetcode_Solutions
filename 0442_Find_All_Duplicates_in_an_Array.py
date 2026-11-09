# Leetcode 442 : Find All Duplicates in an Array
# Difficulty : Medium

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res=[]
        hs=set()
        for i in nums:
            if i in hs:
                res.append(i)
            else:
                hs.add(i)
        return res