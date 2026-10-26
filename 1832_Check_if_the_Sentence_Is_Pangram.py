# Leetcode 1832 : Check if the Sentence Is Pangram
# Difficulty: Easy

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence_set=set(sentence.lower())
        alphabet_set=set(string.ascii_lowercase)
        return alphabet_set.issubset(sentence_set)