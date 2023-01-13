#include <bits/stdc++.h>
using namespace std;

long long dp[1000];
long long solve(long long n)
{ // base case
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 2;
    for(int i=4; i<=n; i++)
        dp[i] = dp[i-1] + dp[i-3] + dp[i-4];
    return dp[n];
}

// long long dp[1000];
// long long solve(int n){    
//     if (n < 0)
//         return 0;
//     if (n == 0)
//         return 1;
//     if (dp[n]!=0)
//         return dp[n];
//     return dp[n] = solve(n-1) + solve(n-3) + solve(n-4);
// }

int main(){
    long long n;
    cin >> n;
    
    cout << solve(n);
    return 0;
}

