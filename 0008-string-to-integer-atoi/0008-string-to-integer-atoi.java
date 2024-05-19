class Solution {
    public int myAtoi(String s) {
        // return 0 if the length of s is 0
        if (s.length() == 0) {
            return 0;
        }
        boolean positive = true;
        short i = 0;
        // ignoring any leading whitespace
        while (i < s.length() && s.charAt(i) == ' ') {
            i++;
        }
        // determine signedness
        if (i < s.length() && (s.charAt(i) == '-' || s.charAt(i) == '+')) {
            positive = (s.charAt(i) != '-');
            i++;
        }
        // start reading in numbers
        int num = 0;
        long check;
        while (i < s.length() && s.charAt(i) >= '0' && s.charAt(i) <= '9') {
            // positive overflow
            if (positive) {
                check = ((long)num * 10) + (s.charAt(i) - '0');
                if (check > Integer.MAX_VALUE) {
                    return Integer.MAX_VALUE;
                } else {
                    num *= 10;
                    num += (s.charAt(i) - '0');
                }
            }
            // negative overflow
            else {
                check = ((long)num * 10) - (s.charAt(i) - '0');
                if (check < Integer.MIN_VALUE) {
                    return Integer.MIN_VALUE;
                } else {
                    num *= 10;
                    num -= (s.charAt(i) - '0');
                }
            }
            i++;
        }
        return num;
    }
}