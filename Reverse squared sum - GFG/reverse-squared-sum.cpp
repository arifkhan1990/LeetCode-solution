#include<bits/stdc++.h>
using namespace std;
int main()
 {
	int tc, n, m;
	cin >> tc;
	while(tc--){
	  cin >> n ;
	  m = n;
	  long long ans = 0, a;
	  vector<long long> ab, ba;
    	  while(n--){
    	      cin >> a;
    	      ab.push_back(a);
    	  }
    	  int k = 1;
    	  for(int i = m-1 ; i >= 0; i--){
    	      ba.push_back(ab[i]*ab[i]);
    	  }
    	  for(auto i : ba){
    	      if(k){
    	          ans += i;
    	           k = 0;
    	      }else{
    	          ans -= i;
    	          k = 1;
    	      }
    	  }
    	  cout << ans << endl;
	  }
	return 0;
}