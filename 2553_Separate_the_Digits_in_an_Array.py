# Leetcode 2553 : Separate the Digits in an Array
# Difficulty : Easy

class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res=[]
        for i in range(len(nums)-1,-1,-1):
            val=nums[i]
            while val>0:
                res.append(val%10)
                val//=10
        res.reverse()
        return res

        '''
        # String Conversion Method
        res=[]
        for i in nums:
            for ch in str(i):
                res.append(int(ch))
        return res
        '''