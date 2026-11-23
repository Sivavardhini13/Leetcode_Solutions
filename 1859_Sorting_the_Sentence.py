# Leetcode 1859 : Sorting the Sentence
# Difficulty : Easy

class Solution:
    # Hashmap Approach
    def sortSentence(self, s: str) -> str:
        d = {}
        for word in s.split():
            d[int(word[-1])] = word[:-1]
        ans = []
        for i in range(1, len(d) + 1):
            ans.append(d[i])
        return " ".join(ans)