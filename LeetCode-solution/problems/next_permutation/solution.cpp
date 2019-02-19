class Solution {
public:
    void nextPermutation(vector<int>& nums) {
       // sort(nums.begin(),nums.end());
        
        while(next_permutation(nums.begin(),nums.end())){
            cout << "[";
            for(int i = 0; i < nums.size() ; i++){
                cout << nums[i];
                if(i != nums.size() -1)
                    cout << ",";
            }
            cout << "]" << endl;
            break;
        }
    }
};