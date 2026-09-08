# Leetcode 3895 : Count Digit Appearances
# Difficulty : Medium

class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        s=''.join(map(str,nums))
        return s.count(str(digit))