class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        results = {target: [-1]} # string : [indices with it]

        for i in range(len(nums)):
            num = nums[i]
            if results.get(num) is None:
                results[num] = [i]
            else:
                results[num].append(i)
        
        pairs = 0
        for i in range(len(nums)):
            num = nums[i]
            # get the remaining substring
            j = 0
            while j < len(num) and j < len(target):
                if num[j] == target[j]:
                    j += 1
                else:
                    break
            remainder = target[j:]
            if results.get(remainder) is None:
                continue
            if results.get(num + remainder) is None and results.get(remainder + num) is None:
                continue
            else:
                for res in results.get(remainder):
                    if res != i:
                        pairs += 1
        return pairs