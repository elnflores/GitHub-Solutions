class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        # loop through the array of ints
        for i in range(len(nums)):
            # take our target, and subtract the current int
            cmp = target - nums[i]
            if cmp in hashmap:
                # if we find a matching int, we can return their indices
                return [i, hashmap[cmp]]
            # if not, add to hashmap in case we need it later
            hashmap[nums[i]] = i
        