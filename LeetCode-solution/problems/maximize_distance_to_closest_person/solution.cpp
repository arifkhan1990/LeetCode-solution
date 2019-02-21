class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int ans = 1;
        for(int i = 0; i < seats.size(); i++) {
            if(seats[i] == 0) {
                int disL = 0,disR = 0,j = i;
                while( j+1 < seats.size() and !seats[++j]) {
                    disL++;
                }
                if(seats[j] == 1) disL++;
                j=i;
                while( j-1 >=0 and !seats[--j]) {
                    disR++;
                }
                if(seats[j] == 1) disR++;
               // cout <<seats[i] << " - " <<  disL << " , " << disR << endl;
                if(disL == 0)
                    ans = max(ans,disR);
                else if(disR == 0)
                    ans = max(ans,disL);
                else
                    ans = max(ans,min(disL,disR));
            }
        }
        return ans;
    }
};