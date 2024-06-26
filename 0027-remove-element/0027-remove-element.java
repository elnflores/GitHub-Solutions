class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0, k = 0;
        for (; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }
}