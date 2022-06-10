class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        d = {"X--":0,
            "X++":0,
             "--X":0,
             "++X":0}
        for i in operations:
            if i in d.keys():
                d[i] += 1
        return d["X++"] + d["++X"] - d["--X"] - d["X--"]