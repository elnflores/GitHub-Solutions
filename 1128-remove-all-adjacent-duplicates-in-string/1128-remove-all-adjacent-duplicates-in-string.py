class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = [] # stack
        for ch in s:
            if len(result) == 0 or result[len(result)-1] != ch:
                result.append(ch)
            else:
                result.pop()
        return "".join(result)