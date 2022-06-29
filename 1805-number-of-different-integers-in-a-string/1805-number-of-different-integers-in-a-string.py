import re
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = re.sub('[a-zA-Z]',' ', word)
        return len(set(int(i) for i in word.split()))