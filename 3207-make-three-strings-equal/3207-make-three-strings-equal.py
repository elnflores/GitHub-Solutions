class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        lcp = 0
        l1, l2, l3 = len(s1), len(s2), len(s3)
        while (lcp < l1 and lcp < l2 and lcp < l3 and s1[lcp] == s2[lcp] and s2[lcp] == s3[lcp]):
            lcp += 1
        if lcp == 0:
            return -1
        return (l1 - lcp) + (l2 - lcp) + (l3 - lcp)
