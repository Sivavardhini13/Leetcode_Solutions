# Leetcode 1464 : Maximum Product of Two Elements in an Array
# Difficulty : Easy

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # Sorting
        nums.sort(reverse=True)
        return (nums[0]-1)*(nums[1]-1)
        
        '''
        # Brute force
        n=len(nums)
        maxProd=0
        for i in range(n):
            for j in range(i+1,n):
                prod=(nums[i]-1)*(nums[j]-1)
                maxProd=max(maxProd,prod)
        return maxProd
        '''