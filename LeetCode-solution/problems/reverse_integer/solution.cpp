class Solution {
public:
    int reverse(int x) {
        long long nu = 0;
     while(x != 0){
         nu = x % 10 + nu * 10;
         x/=10;
         if( nu > INT_MAX  || nu < INT_MIN )
         return 0;
     }
        return (int)nu;
    }
};