class Solution {
public:
 void permutation(vector<vector<int>>& ans, vector<int>& nums, int s, int e) {
        if(s == e+1) {
            ans.push_back(vector<int>(nums));
            return;
        }
        for(int i = s; i <= e; i++) {
            swap(nums[s],nums[i]);
            permutation(ans,nums,s+1,e);
            swap(nums[s],nums[i]);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        
        int s = nums.size();
        
        permutation(ans , nums, 0, s-1);
        return ans;
    }
    
};