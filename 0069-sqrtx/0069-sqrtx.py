class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(0, x + 1):
            if i * i < x:
                continue
            if i * i == x:
                return i
            else:
                return i - 1