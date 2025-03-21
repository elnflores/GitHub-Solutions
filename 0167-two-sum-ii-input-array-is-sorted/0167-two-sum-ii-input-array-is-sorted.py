class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in numbers:
                ind = numbers.index(diff)
                if ind != i:
                    if i > 0 and numbers[i - 1] == numbers[i]:
                        return [ind + 1, i + 1]
                    return [i + 1, ind + 1]