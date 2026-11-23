# Leetcode 2042 : Check if Numbers Are Ascending in a Sentence
# Difficulty : Easy

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # Single Pass - Previous Element Tracking
        prev = 0
        for word in s.split():
            if word.isdigit():
                curr = int(word)
                if curr <= prev:
                    return False
                prev = curr
        return True