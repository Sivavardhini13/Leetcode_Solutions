# LeetCode 9: Palindrome Number
# Difficulty: Easy
# Approach: Reverse Integer
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        original=x
        rev=0
        while x:
            rev=rev*10+x%10
            x//=10
        return original==rev