class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.empty()) return 0;
        size_t p = haystack.find(needle);
        if (haystack.find(needle) != string::npos) {
             return p;
        }else{
           return -1;
        }
    }
};