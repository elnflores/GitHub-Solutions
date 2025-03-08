class Solution:
    def convert(self, s: str, numRows: int) -> str:
        a = {}
        row = 0
        step = 1
        for letter in s:
            if a.get(row) is not None:
                a[row].append(letter)
            else:
                a[row] = [letter]
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        
        string = ""
        for row in a.values():
            for ch in row:
                string += ch
            
        return string