# Leetcode 3668 : Restore Finishing Order
# Difficulty : Easy

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        return [i for i in order if i in friends]