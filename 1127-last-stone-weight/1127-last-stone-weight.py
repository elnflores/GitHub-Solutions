class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = sorted(stones)
        while stones[-2] != 0:
            if stones[-1] == stones[-2]:
                stones[-1] = 0
                stones[-2] = 0
            else:
                stones[-1] = (stones[-1] - stones[-2])
                stones[-2] = 0

            stones = sorted(stones)
        return stones[len(stones)-1]
                

        