# Leetcode 39 : Combination Sum
# Defficulty : Medium

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]
        def backtrack(start, target, comb):
            if target == 0:
                res.append(comb)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                backtrack(i, target-candidates[i], comb+[candidates[i]])
        backtrack(0, target, [])
        return res