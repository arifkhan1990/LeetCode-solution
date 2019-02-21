class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {

        int ls[128] = {0}, use[26] = {0};
        for(int i = 0;i < 26; i++)
              ls[order[i]] = i;
        for(int i = 0, j = 0; i < words.size()-1; i++) {
            string st1 = words[i], st2 = words[i+1];
            for(j = 0; j < st1.size() and j < st2.size(); j++) {
                if(ls[st1[j]] > ls[st2[j]]) {
                        return false;
                }else if(ls[st1[j]] < ls[st2[j]]){
                    break;
                }
            }
            if(--j < st1.size())
                return false;
        }
        return true;
    }
};