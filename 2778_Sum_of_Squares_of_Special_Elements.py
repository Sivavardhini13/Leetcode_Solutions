# Leetcode 2778 : Sum of Squares of Special Elements
# Difficulty : Easy

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # Loop from i+1
        sum=0
        n=len(nums)
        for i in range(n):
            if n%(i+1)==0:
                sum+=nums[i]*nums[i]
        return sum

        '''
        # Loop from [1]
        sum=0
        n=len(nums)
        for i in range(1, n+1):
            if n%i==0:
                sum+=nums[i-1]*nums[i-1]
        return sum
        '''