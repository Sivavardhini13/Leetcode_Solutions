# Leetcode 125 : Valid Palindrome
# Difficulty : Easy

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        res=""
        for i in s:
            if i.isalnum():
                res+=i
        return res==res[::-1]