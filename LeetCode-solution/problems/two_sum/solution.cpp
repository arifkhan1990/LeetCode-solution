class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        vector<int> result(2);
        for (int i=0;i<numbers.size()-1;i++){
            for (int j=i+1;j<numbers.size();j++){
                if (numbers[i]+numbers[j]==target){
                    result[0] = i,result[1] = j;
                    return result;
                }
            }    
        }
        return result;
    }
};
