#include <bits/stdc++.h>
using namespace std;

int minDis(string s1, string s2, int n, int m, vector<vector<int> >& dp){
    if (n == 0)
        return m;
 
    if (m == 0)
        return n;

    if (dp[n][m] != -1)
        return dp[n][m];
 
    if (s1[n - 1] == s2[m - 1]) {
        return dp[n][m] = minDis(s1, s2, n - 1, m - 1, dp);
    }

    else {
        int insert, del, replace; 
 
        insert = minDis(s1, s2, n, m - 1, dp);
        del = minDis(s1, s2, n - 1, m, dp);
        replace = minDis(s1, s2, n - 1, m - 1, dp);
        return dp[n][m]
               = 1 + min(insert, min(del, replace));
    }
}


int main() {
    string str1,str2
    cin >> str1 >> str2;

    vector<vector<int> > dp(str1.length() + 1, vector<int>(str2.length() + 1, -1));
 
    cout << minDis(str1, str2, str1.length(), str2.length(), dp);
    return 0;

}
