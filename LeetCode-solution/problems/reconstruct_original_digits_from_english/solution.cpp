class Solution {
public:
    string originalDigits(string s) {
        vector<int> data(128);
        string res = "";
        for(auto i : s)
            data[i]++;
        int input[10] = {0};
        input[0] = data['z'];
        input[2] = data['w'];
        input[4] = data['u'];
        input[6] = data['x'];
        input[8] = data['g'];
        input[3] = data['h'] - input[8];
        input[5] = data['f'] - input[4];
        input[7] = data['s'] - input[6];
        input[9] = data['i'] - input[5] - input[6] - input[8]; 
        input[1] = data['n'] - input[7] - 2 * input[9];
        for(int i = 0; i < 10; i++)
            for(int j = 0; j < input[i]; j++)
                res += i + '0';

        return res;
    }
};