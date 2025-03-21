class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    cache[i][j] = 1 + cache[i - 1][j - 1]
                else:
                    cache[i][j] = max(cache[i][j - 1], cache[i - 1][j])
        
        return cache[len(text1)][len(text2)]
