# Leetcode 2243. Calculate Digit Sum of a String
# Difficulty : Easy

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ""

            for i in range(0, len(s), k):
                digit_sum = 0
                group = s[i:i+k]

                for digit in group:
                    digit_sum += int(digit)

                new_s += str(digit_sum)

            s = new_s

        return s