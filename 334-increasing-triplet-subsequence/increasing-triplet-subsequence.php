class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function increasingTriplet($nums) {
        $n1 = $n2 = PHP_INT_MAX;
        foreach ($nums as $x){
            if ($x <= $n1){
                $n1 = $x;
            }elseif($x <= $n2) {
                $n2 = $x;
            }else {
                return 1;
            }
        }
        return 0;
    }
}