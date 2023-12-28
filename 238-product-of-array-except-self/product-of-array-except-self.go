func productExceptSelf(nums []int) []int {
    n:= len(nums)
    ans := make([]int, n)
    for i := range ans {
        ans[i] = 1
    }
    
    l_p := 1
    for i:= 0; i<n; i++ {
        ans[i] *= l_p
        l_p *= nums[i]
    }

    r_p := 1
    for i:= n-1; i > -1; i-- {
        ans[i] *= r_p
        r_p *= nums[i]
    }

    return ans
}