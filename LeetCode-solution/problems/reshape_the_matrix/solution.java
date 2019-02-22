class Solution {
    public int[][] matrixReshape(int[][] nums, int r, int c) {
        int [][] ar = new int[r][c];
        int c2 = 0, rr = 0;
        if(c*r != nums.length * nums[0].length ) return nums;
        for (int r1 = 0; r1 < nums.length; ++r1)
            for (int c1 = 0; c1 < nums[0].length; ++c1){
                if(c2 == c) {
                    c2 = 0;
                    rr++;
                }
                
                ar[rr][c2++] = nums[r1][c1];
            }
        return ar;
    }
}