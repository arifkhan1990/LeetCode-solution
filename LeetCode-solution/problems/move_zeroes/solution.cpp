class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int>ans;
        int n = 0;
              
        for(int i = 0; i < nums.size();i++){
          if(nums[i] != 0) {
              swap(nums[n++], nums[i]);
          }
        }
    }
};