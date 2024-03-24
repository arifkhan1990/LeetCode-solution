class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findDuplicate($nums) {
        $slow = 0;
        $fast = 0;

        while (1) {
            $slow = $nums[$slow];
            $fast = $nums[$nums[$fast]];
            if ($slow == $fast){
                break;
            } 
        }

        $slow = 0;
        while($slow != $fast) {
            $slow = $nums[$slow];
            $fast = $nums[$fast];
        }

        return $slow;
    }
}