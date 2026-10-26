# Leetcode 1512 : Number of Good Pairs
# Difficulty: Easy

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i]==nums[j] and i<j:
                    count+=1
        return count