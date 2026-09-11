# Leetcode 3483 : Unique 3-Digit Even Numbers
# Difficulty : Easy

from itertools import permutations
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        nums=set()
        for a,b,c in permutations(digits,3):
            if a!=0 and c%2==0:
                nums.add((a,b,c))
        return len(nums)