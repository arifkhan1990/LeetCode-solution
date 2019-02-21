
class Solution {
public:
    vector<string> letterCasePermutation(string S) {
        vector<string> ans;
        int len = 0;
        for(auto x : S) 
            if(isalpha(x)) len++;
        
        for(int i = 0; i < (1 << len); i++) {
            string w = "";
            int j = 0;
            for(auto x : S) {
                if(isalpha(x)) {
                    if(((i >> j++) & 1) == 1) {
                        w.push_back(tolower(x));
                    }else {
                         w.push_back(toupper(x));
                    }
                }else {
                     w.push_back(x);
                }
            }
            ans.push_back(w);  
        }

        return ans;
    }
};