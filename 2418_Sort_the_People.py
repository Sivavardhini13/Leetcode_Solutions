# Leetcode 2418 : Sort the People
# Difficulty : Easy

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        dict={heights[i]: names[i] for i in range(len(names))}
        heights.sort()
        res=[]
        for height in reversed(heights):
            res.append(dict[height])
        return res