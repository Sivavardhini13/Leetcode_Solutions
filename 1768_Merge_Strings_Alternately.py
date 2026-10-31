# Leetcode 1768 : Merge Strings Alternately
# Difficulty : Easy

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Zip Approach
        merged=[]
        for a,b in zip(word1,word2):
            merged.append(a+b)
        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])
        return "".join(merged)

        '''
        # Two-Pointer Approach
        i,j=0,0
        res=[]
        while i<len(word1) and j<len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        return "".join(res)
        '''