class Solution {
    public int lengthOfLastWord(String s) {
        String[] arr = s.split(" ", 0);
        int len = arr[arr.length - 1].length();
        //arr = null;
        return len;
    }
}