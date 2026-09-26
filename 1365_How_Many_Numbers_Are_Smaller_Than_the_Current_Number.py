# Leetocde 1365 : How Many Numbers Are Smaller Than the Current Number
# Difficulty : Easy

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        res=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    c+=1
            res.append(c)
        return res