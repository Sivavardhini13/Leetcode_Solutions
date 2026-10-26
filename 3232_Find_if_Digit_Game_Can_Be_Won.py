# Leetcode 3232 : Find if Digit Game Can Be Won
# Difficulty : Easy

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        count1, count2=0, 0
        for i in nums:
            if i<10:
                count1+=i
            else:
                count2+=i
        return count1!=count2