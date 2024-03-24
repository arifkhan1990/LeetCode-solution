class Solution {

    /**
     * @param String $s
     * @return String
     */
    function reverseWords($s) {
        $s = trim($s);
        $s = preg_replace('/\s+/', ' ', $s);
        $ans = array_reverse(explode(" ", $s));
        return implode(" ", $ans);
    }
}