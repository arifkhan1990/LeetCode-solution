class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int>ans;
        
        int t = 1,p = k+1;
        for(; t <= p ;){
            ans.push_back(t++);
                if(t <= p)ans.push_back(p--);
            }
        for (int i = k+2; i <= n; i++)
            ans.push_back(i);
        
        return ans;
    }
};