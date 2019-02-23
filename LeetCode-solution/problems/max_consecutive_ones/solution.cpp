class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ans = 0;
        for(int i = 0; i < nums.size(); i++) {
            int one = 0;
            while(i < nums.size() and nums[i]) {
                    one++;
                i++;
            }
            ans = max(ans,one);
        }
        return ans;
    }
};