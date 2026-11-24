# Leetcode 1979 : Find Greatest Common Divisor of Array
# Difficulty : Easy

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        '''
        # Brute Force
        mn = min(nums)
        mx = max(nums)
        ans = 1
        for i in range(1, mn + 1):
            if mn % i == 0 and mx % i == 0:
                ans = i
        return ans

        # Eulclidian Algorithm
        mn = min(nums)
        mx = max(nums)
        while mn != 0:
            mx, mn = mn, mx % mn
        return mx
        '''

        # 1 - liner
        return gcd(min(nums), max(nums))