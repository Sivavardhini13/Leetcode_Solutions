# Leetcode 3498 : Reverse Degree of a String
# Difficulty : Easy

class Solution:
    def reverseDegree(self, s: str) -> int:
        ans, i = 0, 1
        for ch in s:
            ans += (123 - ord(ch)) * i
            i += 1
        return ans

        '''
        # My first solution
        ans = 0
        for i in range(len(s)):
            c = s[i]
            pos = ord(c) - ord('a') + 1
            reverse_pos = 27 - pos
            ans += reverse_pos * (i + 1)

        return ans
        '''