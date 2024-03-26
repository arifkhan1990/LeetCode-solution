class Solution {

    /**
     * @param Integer[] $nums
     * @return NULL
     */
    function moveZeroes(&$nums) {
        $n = 0;
        $m = 0;
        while ($m < count($nums)) {
            if ($nums[$m] != 0) {
                [$nums[$n], $nums[$m]] = [$nums[$m], $nums[$n]];
                $n++;
            }
            $m++;
        }
    }
}