class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        lcp = 0
        r = min(len(s1), len(s2), len(s3))
        for i in range(r):
            if (s1[i] == s2[i] and s2[i] == s3[i]):
                lcp += 1
            else:
                break
        if lcp == 0:
            return -1
        diffs = len(s1[lcp:len(s1)]) + len(s2[lcp:len(s2)]) + len(s3[lcp:len(s3)])
        if lcp == 0:
            return -1
        else:
            return diffs
