#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,m;
    cin >> n >> m;
    bool prime[m + 1];
    memset(prime, true, sizeof(prime));
 
    for (int p = 2; p * p <= m; p++) {
        if (prime[p] == true) {
            for (int i = p * p; i <= m; i += p)
                prime[i] = false;
        }
    }
    
    int co = 0;
    for (int p = n; p <= m; p++){
        if (prime[p]){
            co ++;
        }
    }
    cout << co << endl;
    return 0;
}