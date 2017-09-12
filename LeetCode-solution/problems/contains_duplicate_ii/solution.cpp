class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        set<int>ans;
        for(int i = 0; i < nums.size() ; i++){
            if(i > k) ans.erase(nums[i - k - 1]);
                    if(!ans.insert(nums[i]).second) return true;
        }
        return false;
    }
};