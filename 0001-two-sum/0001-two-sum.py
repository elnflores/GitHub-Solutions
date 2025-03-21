class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {} # val : index
        for i in range(len(nums)):
            val = nums[i]

            if vals.get(val) == None:
                vals[val] = i

            diff = target - val
            if vals.get(diff) != None and vals.get(diff) != i:
                return [i, vals.get(diff)]


        