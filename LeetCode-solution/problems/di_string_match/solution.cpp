class Solution {
public:
    vector<int> diStringMatch(string S) {
        int n = S.size(), ic = 0, id = n;
        vector<int> ans(n+1);
        for(int i = 0; i < n; i++) {
            ans[i] = S[i] == 'I' ? ic++: id--;
        }
        ans[n] = ic;
        return ans;
    } 
};