class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            rep = (columnNumber - 1) % 26
            result.append(chr(ord('A') + rep))
            columnNumber = (columnNumber - 1) // 26
        return "".join(reversed(result))