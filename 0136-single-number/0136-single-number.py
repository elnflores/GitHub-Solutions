class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR: 0, num = 100, res = 100
        # XOR: 100, num = 001, res = 101
        # XOR: 101, num = 010, res = 111
        # XOR: 111, num = 001, res = 110
        # XOR: 110, num = 010, res = 100

        comp = 0
        for num in nums:
            comp ^= num
        return comp
        