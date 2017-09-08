class Solution {
public:
    int romanToInt(string s) {
        map<char,int>data = {{ 'I' , 1 },
                             { 'V' , 5 },
                             { 'X' , 10 },
                             { 'L' , 50 },
                             { 'C' , 100 },
                             { 'D' , 500 },
                             { 'M' , 1000 }};
        int ans = 0;
        for(int i = 0; i < s.size() ; i++){
        if(data[s[i]] < data[s[i+1]])ans -= data[s[i]];
        else  ans += data[s[i]];
        }
        return ans;
    }
};