func construct2DArray(original []int, m int, n int) [][]int {
    var ans [][] int;

    if n*m == len(original) {
        for i := 0; i < m; i++ {
            ans = append(ans, original[i*n: (i+1)*n])
        }
    }
    return ans;
}