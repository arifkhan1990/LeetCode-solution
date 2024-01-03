func minKBitFlips(nums []int, k int) int {
    n := len(nums)
    fc := 0
    fq := make([]int, 0)

    for i:= 0; i<n ; i++ {
        if len(fq) > 0 && i >= fq[0]+k {
            fq = fq[1:]
        }

        if (nums[i] + len(fq)) %2 == 0 {
            fc++
            fq = append(fq, i)
            if  i+k > n {
                return -1
            }
        }
    }
    return fc
}