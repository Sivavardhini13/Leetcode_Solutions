# Leetcode 3731 : Find Missing Elements
# Difficulty : Easy

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn = min(nums)
        mx = max(nums)
        ans = []
        seen = set(nums)
        return [x for x in range(mn, mx+1) if x not in seen]