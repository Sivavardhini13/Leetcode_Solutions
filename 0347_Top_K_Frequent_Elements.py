# Leetcode 347 : Top K Frequent Elements
# Difficulty : Medium

import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dict={}
        for num in nums:
            dict[num]=dict.get(num,0)+1
        return heapq.nlargest(k,dict.keys(),key=dict.get)