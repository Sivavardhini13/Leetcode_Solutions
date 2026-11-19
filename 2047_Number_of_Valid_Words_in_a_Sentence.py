# Leetcode 2047 : Number of Valid Words in a Sentence
# Difficulty : Easy

class Solution:
    def countValidWords(self, sentence: str) -> int:
        def fn(word):
            seen = False
            for i, ch in enumerate(word):
                if ch.isdigit() or (ch in "!.," and i != len(word)-1):
                    return False
                elif ch == '-':
                    if seen or i == 0 or i == len(word)-1 or not word[i+1].isalpha():
                        return False
                    seen = True
            return True
        return sum(fn(word) for word in sentence.split())

        '''
        # Regex Approach
        pattern = re.compiler(r'(^[a-z]+(-[a-z]+)?)?[,.!]?$')
        return sum(bool(pattern.match(word))for word in sentence.split())
        '''