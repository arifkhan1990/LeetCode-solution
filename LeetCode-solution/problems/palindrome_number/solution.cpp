class Solution {
public:
    bool isPalindrome(int x) {
        long long nu = 0,x1;
        x1 = x;
     while(x != 0){
         nu = x % 10 + nu * 10;
         x/=10;
         if( nu > INT_MAX  || nu < INT_MIN )
         return 0;
     }
        return (x1 == nu and x1 >= 0)? true : false;
    }
};