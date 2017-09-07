class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
           bool ar[1000001] ;
        memset(ar,false,sizeof(ar));
        for(int i = 0; i < nums.size() ; i++){
        	if(nums[i] > 0)
        	   ar[nums[i]] = true;
        }
        int n = sizeof(ar)/sizeof(ar[0]);
        for(int i = 1;  i <= n; i++){
        	if(!ar[i]){
        	   return i;
        	}
        }
    }
};