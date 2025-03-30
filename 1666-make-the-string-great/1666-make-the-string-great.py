class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 0:
            return ""
        stack = [s[0]]
        for i in range(1, len(s)):
            ch = s[i]
            if len(stack) == 0:
                stack.append(ch)
            
            elif stack[-1].islower() and ch == stack[-1].upper():
                stack.pop()
            elif stack[-1].isupper() and ch == stack[-1].lower():
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
