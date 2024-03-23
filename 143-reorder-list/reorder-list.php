/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {

    /**
     * @param ListNode $head
     * @return NULL
     */
    function reorderList($head) {
        if(!$head) return;

        $slow = $fast = $head;
        while ($fast && $fast->next) {
            $slow = $slow->next;
            $fast = $fast->next->next;
        }

        $prev = null;
        while ($slow) {
            $nextNode = $slow->next;
            $slow->next = $prev;
            $prev = $slow;
            $slow = $nextNode;
        }

        $first = $head;
        $second = $prev;

        while ($second->next) {
            $temp1 = $first->next;
            $first->next = $second;
            $temp2 = $second->next;
            $second->next = $temp1;
            $first = $temp1;
            $second = $temp2;
        }
    }
}