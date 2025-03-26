class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = [] # stack
        for ch in s:
            if len(result) == 0:
                result.append(ch)
            else:
                if result[len(result)-1] == ch:
                    while len(result)>0 and result[len(result)-1] == ch:
                        result.pop()
                else:
                    result.append(ch)
        return "".join(result)


            