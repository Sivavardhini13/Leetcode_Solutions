# Leetcode 1331 : Rank Transform of an Array
# Difficulty : Easy

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # sorting + hashmap approach
        sorted_arr = sorted(set(arr))
        rank = {}
        for i, num in enumerate(sorted_arr):
            rank[num] = i + 1
        return [rank[num] for num in arr]