# Leetcode 46 : Permutations
# Difficulty : Medium

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        perms = []
        sol = []

        def backtrack():
            if len(nums) == len(sol):
                perms.append(sol[:])
                return

            for i in nums:
                if not i in sol:
                    sol.append(i)
                    backtrack()
                    sol.pop()

        backtrack()
        return perms