class Solution {
    public int lengthOfLastWord(String s) {
        String[] arr = s.split(" ", 0);
        if (arr.length == 0) {
            return 0;
        }
        return arr[arr.length - 1].length();
    }
}