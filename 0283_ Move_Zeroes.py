# Leetcode 283 : Move Zeroes
# Difficulty : Easy

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        new_nums=[]
        count=0
        for num in nums:
            if num!=0:
                new_nums.append(num)
            else:
                count+=1