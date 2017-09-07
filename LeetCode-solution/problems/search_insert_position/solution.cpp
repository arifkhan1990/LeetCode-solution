class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int i,sz;
        for(i = 0, sz = nums.size() ; i < sz ; i++){
            if(nums[i] >= target)
                return i;
        }
        return i;
    }
};