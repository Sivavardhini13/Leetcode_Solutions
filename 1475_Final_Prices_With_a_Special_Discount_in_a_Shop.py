# Leetcode 1475 : Final Prices With a Special Discount in a Shop
# Difficulty : Easy

class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        res=prices.copy()
        stack=deque()
        for i in range(len(prices)):
            while stack and prices[stack[-1]]>=prices[i]:
                res[stack.pop()]-=prices[i]
            stack.append(i)
        return res