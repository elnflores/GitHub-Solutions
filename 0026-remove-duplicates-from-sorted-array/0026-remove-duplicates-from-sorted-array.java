class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 1, k = 0;
        for (; i < nums.length; i++) {
            if (nums[i] != nums[k]) {
                nums[++k] = nums[i];
            }
        }
        return k + 1;        
    }
}