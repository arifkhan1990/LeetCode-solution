class Solution {
public:
    string getPermutation(int n, int k) {
        string ans = "";
        string res = "123456789";
        int arr[10]={1};
        for(int i = 1; i < 10; i++){
            arr[i] = arr[i-1]*i;
        }
        
        --k;
        for(int i = n; i >= 1; --i) {
            int j = k / arr[i - 1];
            k %= arr[i - 1];
            ans.push_back(res[j]);
            res.erase(j, 1);
        }
        return ans;
    }
};