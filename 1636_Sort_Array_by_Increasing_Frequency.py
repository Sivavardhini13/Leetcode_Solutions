# Leetcode 1636 : Sort Array by Increasing Frequency
# Difficulty : Easy

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq={}
        for item in nums:
            freq[item]=freq.get(item,0)+1
        res=sorted(nums, key=lambda x: (freq[x], -x))
        return res