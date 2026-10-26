# Leetcode 2108 : Find First Palindromic String in the Array
# Difficulty : Easy

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for i in words:
            if i==i[::-1]:
                return i
        return ""