class Solution {
public:
    int lengthOfLastWord(string s) {
        stringstream str1(s);
        vector < string > variable;
        string take;
        while (str1 >> take)
        variable.push_back(take);
       return variable.empty() ?  0 :  variable[variable.size()-1].size();
    }
};