class Solution {

    /**
     * @param String $num
     * @param Integer $k
     * @return String
     */
    function removeKdigits($num, $k) {
        $s = [];
        foreach (str_split($num) as $d) {
            while ($k > 0 && !empty($s) && end($s) > $d) {
                array_pop($s);
                $k--;
            }
            $s[] = $d;
        }

        while ($k > 0) {
            array_pop($s);
            $k--;
        }

        while (!empty($s) && $s[0] == '0') {
            array_shift($s);
        }

        return empty($s) ? '0' : implode('', $s);
    }
}