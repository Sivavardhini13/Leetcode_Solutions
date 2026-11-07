# Leetcode 409. Longest Palindrome
# Difficulty : Easy

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Dict Approach
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        length=0
        odd_found=False
        for count in freq.values():
            if count%2==0:
                length+=count
            else:
                length+=count-1
                odd_found=True
        if odd_found:
            length+=1
        return length

        '''
        # Set Approach
        seen=set()
        length=0
        for ch in s:
            if ch in seen:
                length+=2
                seen.remove(ch)
            else:
                seen.add(ch)
        return length+1 if seen else length
        '''