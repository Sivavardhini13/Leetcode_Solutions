# Leetcode 2114 : Maximum Number of Words Found in Sentences
# Difficulty : Easy

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max(s.count(" ")+1 for s in sentences)