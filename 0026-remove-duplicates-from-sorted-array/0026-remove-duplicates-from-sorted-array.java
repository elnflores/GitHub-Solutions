class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0, k = 0, prev = 101;

        for (; i < nums.length; i++) {
            if (nums[i] != prev) {
                nums[k++] = nums[i];
                prev = nums[i];
            }
        }
        return k;        
    }
}