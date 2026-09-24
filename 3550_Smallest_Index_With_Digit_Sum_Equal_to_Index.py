# Leetcode 3550 : Smallest Index With Digit Sum Equal to Index
# Difficulty : Easy

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum = 0
            while nums[i] > 0:
                sum += nums[i] % 10
                nums[i] //= 10
            if sum == i:
                return i
        return -1

        '''
        # String Conversion Approach
        for i in  range(len(nums)):
            if sum(map(int, str(nums[i]))) == i:
                return i

        return - 1
        '''