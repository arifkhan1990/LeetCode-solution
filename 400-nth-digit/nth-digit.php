class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function findNthDigit($n) {
        $l = 1;
        $s = 1;
        $cnt = 9;

        while ($n > $l*$cnt) {
            $n -= $l * $cnt;
            $l++;
            $cnt *= 10;
            $s *= 10;
        }

        $s += floor(($n-1)/$l);
        return intval(strval($s)[($n-1)%$l]);
    }
}