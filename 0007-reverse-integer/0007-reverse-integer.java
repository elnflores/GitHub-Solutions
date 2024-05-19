class Solution {
    public int reverse(int x) {
        if (x == 0) {
            return 0;
        }
        int num = 0;
        long check;
        while (x != 0) {
            // check for overflow
            check = ((long) num * 10) + (num % 10);
            if (check < Integer.MIN_VALUE || check > Integer.MAX_VALUE) {
                return 0;
            }
            // reverse number
            num *= 10;
            num += x % 10;
            x /= 10;
        }
        return num;
    }
}