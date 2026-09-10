# Leetcode 3871 : Count Commas in Range II
# Difficulty : Medium

class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        ans=0
        x=1000
        while x<=n:
            ans+=n-x+1
            x*=1000
        return ans