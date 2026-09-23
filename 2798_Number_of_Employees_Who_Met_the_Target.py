# Leetcode 2798 : Number of Employees Who Met the Target
# Difficulty : Easy

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c=0
        for i in hours:
            if i>=target:
                c+=1
        return c