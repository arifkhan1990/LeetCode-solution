class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int a = nums.size();
        a = (a * (a+1))/2;
        int sum = 0;
        for(int x : nums)
            sum += x;
        return a - sum;
    }
};