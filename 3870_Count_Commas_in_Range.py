# Leetcode 3870 : Count Commas in Range
# Difficulty : Easy

class Solution:
    def countCommas(self, n: int) -> int:
        num=len(str(n))
        c=0
        if n<1000:
            return 0
        else:
            return n-1000+1