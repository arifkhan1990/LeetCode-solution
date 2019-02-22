class Solution {
public:
    bool isMonotonic(vector<int>& A) {
      bool ac = true,dc = true;
        for(int i = 0; i < A.size()-1; i++) {
            if(A[i] > A[i+1]) ac = false;
            if(A[i] < A[i+1]) dc = false;
        }
        //cout << ac << " = " << dc << endl;
        if(ac || dc) return true;
        return false;
    }
};