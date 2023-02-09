#include <bits/stdc++.h>
using namespace std;

int editDistDP(string str1, string str2, int m, int n){
    int dp[m+1][n+1];
    for (int i=0; i<=m; i++){
        for (int j=0; j<=n; j++){
            if (i==0)
                dp[i][j] = j; // Min. operations = j
            else if (j==0)
                dp[i][j] = i; // Min. operations = i
            else if (str1[i-1] == str2[j-1])
                dp[i][j] = dp[i-1][j-1];
            else
                dp[i][j] = 1 + min({dp[i][j-1],dp[i-1][j],dp[i-1][j-1]}); // Replace
        }
    }
    return dp[m][n];
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    string str1,str2;
    int sub,cost;
    cin >> str1;
    cin >> str2;
    sub = ceil(max(str1.size(),str2.size())/2.0);
    cost = editDistDP(str1,str2,str1.size(),str2.size());
    if (sub <= cost)
        cout << cost << " " << 0;
    else 
        cout << cost << " " << 1;
    // cout << editDistDP(str1,str2,str1.size(),str2.size()) << ;

	return 0;
}