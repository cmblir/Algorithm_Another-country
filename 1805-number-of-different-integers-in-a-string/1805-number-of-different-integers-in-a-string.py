class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        alpha = [i for i in "abcdefghijklnmopqrstuvwxyz"]
        for i in word:
            if i in alpha:
                word = word.replace(i, " ")
        tmp = word.split()
        tmp = [int(i) for i in tmp]
        return len(list(set(tmp))) # 중복을 제거한 리스트의 길이