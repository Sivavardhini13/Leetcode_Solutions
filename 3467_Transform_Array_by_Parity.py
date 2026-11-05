# Leeetcode 3467 : Transform Array by Parity
# Difficulty : Easy

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        nums=[num%2 for num in nums]
        nums.sort()
        return nums