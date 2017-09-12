class Solution {

public:
    int countPrimes(int n) {
        int limit = sqrt(n);
        bool br[n+1];
        memset(br,1,sizeof(br));
        int ans;
        (n > 2)? ans = 1 : ans = 0;
        for(int i = 3; i < n ; i+=2){
            if(br[i]) ans++;
            if(i > limit) continue;
            for(int j = i*i ; j <n ; j+=i)
                br[j] = 0;
        }
        return ans;
    }
};