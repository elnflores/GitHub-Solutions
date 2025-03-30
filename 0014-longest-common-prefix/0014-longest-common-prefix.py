class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = [] # ['f']
        for i in range(200):
            for string in strs:
                if i >= len(string):
                    return "".join(result)
                elif string[i] != strs[0][i]:
                    return "".join(result)
                else:
                    continue
            result.append(strs[0][i])
        return "".join(result)