# Leetcode 1524 : Number of Sub-arrays With Odd Sum
# Difficulty : Medium

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odd = 0
        even = 1
        prefix = 0
        count = 0
        for num in arr:
            prefix += num
            if prefix % 2 == 1:
                count += even
                odd += 1
            else:
                count += odd
                even += 1
        return count % MOD