class Solution:
    def maxPower(self, s: str) -> int:
        counts = {}
        for i in range(len(s)):
            ch = s[i]
        
            if counts.get(ch) == None:
                counts[ch] = [1, 1] # max, cur
            elif ch == s[i-1]:
                counts[ch][1] += 1
                if counts[ch][1] > counts[ch][0]:
                    counts[ch][0] = counts[ch][1]
            else:
                counts[s[i-1]][1] = 0
                counts[ch][1] = 1

        res = -1
        for count in counts:
            if counts[count][0] > res:
                res = counts[count][0]
        return res
