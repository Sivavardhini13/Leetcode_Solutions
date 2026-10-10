# Leetcode 771 : Jewels and Stones
# Difficulty : Easy

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        for i in jewels:
            if i in stones:
                c+=stones.count(i)
        return c