# Leetcode 2913 : Subarrays Distinct Element Sum of Squares I
# Difficulty: Easy

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans,n=0, len(nums)
        for i in range(n):
            seen=set()
            for j in range(i,n):
                seen.add(nums[j])
                count=len(seen)
                ans+=count*count
        return ans