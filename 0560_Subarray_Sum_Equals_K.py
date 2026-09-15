# Leetcode 560 : Subarray Sum Equals K
# Difficulty : Medium

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        count=0
        d={0:1}

        for i in range(len(nums)):
            prefix_sum+=nums[i]

            if prefix_sum-k in d:
                count+=d[prefix_sum-k]
                
            d[prefix_sum]=d.get(prefix_sum,0)+1

        return count