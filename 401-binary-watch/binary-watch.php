class Solution {

    /**
     * @param Integer $turnedOn
     * @return String[]
     */
    function readBinaryWatch($turnedOn) {
        $ans = [];
        for ($h = 0; $h < 12; $h++){
            for ($m = 0; $m < 60; $m++){
                $onCnt = substr_count(decbin($h), '1') + substr_count(decbin($m), '1');
                if ($onCnt == $turnedOn){
                    $t = sprintf("%d:%02d", $h, $m);
                    array_push($ans, $t);
                }
            }
        }
        return $ans;
    }
}