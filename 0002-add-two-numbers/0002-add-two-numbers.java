/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode sum = new ListNode(0);
        ListNode ret = sum;
        while (l1 != null || l2 != null) {
            int ones, tens;
            if (l1 == null && l2 != null) {
                ones = (l2.val + sum.val) % 10;
                tens = (l2.val + sum.val) / 10;
            } else if (l1 != null && l2 == null) {
                ones = (l1.val + sum.val) % 10;
                tens = (l1.val + sum.val) / 10;
            } else {
                ones = (l1.val + l2.val + sum.val) % 10;
                tens = (l1.val + l2.val + sum.val) / 10;
            }
            sum.val = ones;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
            if (!(l1 == null && l2 == null && tens == 0)) {
                sum.next = new ListNode(tens);
                sum = sum.next;
            }
        }
        return ret;
    }
}