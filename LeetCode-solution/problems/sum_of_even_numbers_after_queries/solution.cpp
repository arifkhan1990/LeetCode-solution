class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& A, vector<vector<int>>& queries) {
        vector<int>data;
        int sum = 0;
        for(auto i : A) 
            if( i%2 == 0) sum += i;
        for(int i = 0; i < queries.size(); i++) {
            if(A[queries[i][1]]%2 == 0 ) {
                    sum -= A[queries[i][1]];
            }
            A[queries[i][1]] += queries[i][0];
            if(A[queries[i][1]]%2 == 0 ) {
                    sum += A[queries[i][1]];
            }
                 data.push_back(sum);
        }
        return data;
    }
};