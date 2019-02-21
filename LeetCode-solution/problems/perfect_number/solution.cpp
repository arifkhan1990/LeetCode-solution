class Solution {
public:
    bool checkPerfectNumber(int num) {
        long i = 1, j = 1, sum = 0;
        if(num == 0) return false;
        while(i <= num/2) {
            if(num%i == 0)
                sum += i;
            i++;
        }
        if( sum == num)
            return true;
        return false;
    }
};