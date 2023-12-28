func moveZeroes(nums []int)  {
    z := 0
    nz := 0

    for nz < len(nums) {
        if nums[nz] != 0 {
            nums[z], nums[nz] = nums[nz], nums[z]
            z++
        }
        nz++
    }
}