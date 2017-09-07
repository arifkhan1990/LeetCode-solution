class Solution {
string store(string s){
   string sd;
   for(int i = 0,j; i < s.size();i = j){
   	int l = 1;
   	for(j = i+1 ; s[i] == s[j] ; j++)
   		l++;

   	while(l!=0){
               int p = l%10;
               sd += p+'0';
               l/=10;
   	}
 
   	sd += s[i];
   }
   return sd;
}
public:
    string countAndSay(int n) {
        string res;
            string ar[10001];
            ar[0] = "1";
             for(int i = 1; i < n ; i++){
            	ar[i] = store(ar[i-1]);
            }
            res = ar[n-1] ;
        return res;
    }
};