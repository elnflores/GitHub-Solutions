class Solution:
    def isValid(self, s: str) -> bool:
        result = [] # stack
        opp = {')':'(', '}':'{', ']':'['}
        for ch in s:
            if len(result) == 0:
                result.append(ch)
            else:
                if opp.get(ch) == None:
                    result.append(ch)
                elif opp[ch] == result[len(result)-1]:
                    result.pop()
                else:
                    result.append(ch)
        return len(result) == 0
        