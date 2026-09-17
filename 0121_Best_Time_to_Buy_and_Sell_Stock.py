# Leetcode 121 : Best Time to Buy and Sell Stock
# Difficulty : Easy

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cheapest=prices[0]
        profit=0
        for price in prices:
            if price<cheapest:
                cheapest=price
            if price-cheapest>profit:
                profit=price-cheapest
        return profit