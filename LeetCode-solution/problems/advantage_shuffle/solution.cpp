class Solution {
public:
    vector<int> advantageCount(vector<int>& A, vector<int>& B) {
        multiset<int> res(begin(A), end(A));
        vector<int>ans;
        for(auto b : B) {
            auto it = res.upper_bound(b);
            if(it == res.end())
                it = res.begin();
            ans.push_back(*it);
            res.erase(it);
        }
        return  ans;
    }
};