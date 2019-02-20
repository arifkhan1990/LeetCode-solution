class Solution {
public:
    
    int value(string s) {
        stringstream g(s); 
        
        long num = 0;
        g >> num;
        
        return num;
    }
    
    int calPoints(vector<string>& ops) {
        vector<long> data(1001);
        long sum = 0;
        int p = 0;
        for(int i = 0; i < ops.size() ; i++) {
            string inp = ops[i];
            if(isalpha(inp[0])) {
                if(inp == "C") {
                    p--;
                    sum -= data[p];
                    data.erase(data.begin()+p);
                }else {
                    long res = data[p-1];
                    data[p++] = res*2;
                    sum += data[p-1];;
                }
            }else if(isdigit(inp[0]) or (inp[0] == '-')) {
                data[p++] = value(ops[i]);
                sum += data[p-1];
            }else {
                data[p++] = data[p-1] + data[p-2];
                sum += data[p-1];
            }
        }
        return sum;
    }
};