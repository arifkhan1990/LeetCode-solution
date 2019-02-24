class Solution {
public:
    string maskPII(string S) {
        string ans;
        if(isalpha(S[0])) {
            size_t p = S.find('@');
            p--;
            ans = S[0];
            ans += "*****";
            ans += S[p];
            ans += S.substr(p+1);
            transform(ans.begin(),ans.end(),ans.begin(),::tolower);
        }else {
            int star = 0, zipCode = 0,len = 0;
            for(int i = S.size()-1; i >= 0; i--) {
                if(isdigit(S[i])){
                    len++;
                if(zipCode < 4) {
                    ans += S[i];
                    zipCode++;
                }else {
                    if(zipCode == 4 or star == 3) {
                        ans += '-';
                        if(star == 3) star = 0;
                        zipCode = 5;
                    }
                    ans += "*";
                    star++;
                }
            }
          }
            if(len > 10)
                ans += '+';
            reverse(ans.begin(),ans.end());
        }
        return ans;
    }
};