class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0, k = 0, prev = 10001;
        boolean seenOnce = false;

        for (; i < nums.length; i++) {
            if (nums[i] == prev) {
                if (seenOnce) {
                    nums[k++] = nums[i];
                    seenOnce = false;
                }
            } else {
                nums[k++] = nums[i];
                seenOnce = true;
                prev = nums[i];
            }
        }
        return k;
    }
}