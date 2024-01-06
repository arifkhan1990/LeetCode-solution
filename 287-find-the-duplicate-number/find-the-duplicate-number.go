func findDuplicate(nums []int) int {
    n := len(nums)
    l, r := 1, n-1

    for l < r{
        m := l + (r-l)/2
        cnt := 0

        for _, nm := range nums {
            if nm <= m {
                cnt++
            }
        }

        if cnt > m {
            r = m
        }else {
            l = m + 1
        }
    }
    return l
}