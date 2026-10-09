# Leetcode 3136 : Valid Word
# Difficulty : Easy

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        v,c=0,0
        vow_set='aeiouAEIOU'
        for ch in word:
            if ch.isalpha():
                if ch in vow_set:
                    v+=1
                else:
                    c+=1
            elif not ch.isdigit():
                return False
        return v>0 and c>0