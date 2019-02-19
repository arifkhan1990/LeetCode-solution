class Solution {
public:
 void permutation(vector<vector<int>>& ans, vector<int>& nums, int s, int e) {
        if(s == e+1) {
            ans.push_back(vector<int>(nums));
            return;
        }
     char b[256] = {'0'};
        for(int i = s; i <= e ; i++) {
            if(!b['0'+nums[i]]){
            swap(nums[s],nums[i]);
            permutation(ans,nums,s+1,e);
            swap(nums[s],nums[i]);
            b['0'+nums[i]] = 1;
            }
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> ans;
        
        int s = nums.size();
        permutation(ans , nums, 0, s-1);
        return ans;
    }
};