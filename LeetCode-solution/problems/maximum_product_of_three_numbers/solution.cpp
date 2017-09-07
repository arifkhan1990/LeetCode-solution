class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        long long ans1 ,ans2;
        ans1 = nums[nums.size()-3]*nums[nums.size()-2]*nums[nums.size()-1];
        ans2 = nums[nums.size()-1]*nums[1]*nums[0];
        return ans1 > ans2 ? ans1 : ans2;
    }
};