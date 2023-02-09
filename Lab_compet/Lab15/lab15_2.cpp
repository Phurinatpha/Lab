#include <bits/stdc++.h>
using namespace std;

int cost(int n, int c, vector<int> &cuts){
    
    cuts.push_back(n);
    cuts.insert(cuts.begin(),0);
    sort(cuts.begin(),cuts.end());
    
    vector<vector<int>> dp(c+2,vector<int>(c+2,0));
    for(int i=c; i>=1; i--){
        for(int j=1; j<=c; j++){
            if(i>j)
                continue;
            
            int mini = INT_MAX;
            
            for(int ind=i; ind<=j; ind++){
                int ans = cuts[j+1] - cuts[i-1] + dp[i][ind-1] + dp[ind+1][j];
                mini = min(mini, ans);
            }
            dp[i][j] = mini;
        }
    }
    
    return dp[1][c];

}

int main() {
	
	vector<int> cuts;
	
	int c,n;
    cin >> n;
    cin >> c;
    for (int i=0;i<c;i++){
        int s;
        cin >> s;
        cuts.push_back(s);
    }

	cout << cost(n,c,cuts);
	
	return 0;
}
