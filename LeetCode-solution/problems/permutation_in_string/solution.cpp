class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int l1 = s1.size(), l2 = s2.size(), pur = l1, l = 0;
        
        int ans[128] = {0};
        
        for(auto x : s1) ans[x]++;
        
        for(int i = 0; i < l2; i++) {
            if(ans[s2[i]]-- > 0){
                pur--;
            }
            while(pur == 0) {
                if( i - l + 1 == l1) 
                    return true;
                if(++ans[s2[l++]] > 0) 
                    pur++;
            }
        }
        return false;
    }
};