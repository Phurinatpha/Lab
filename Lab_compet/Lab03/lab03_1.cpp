#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,res = 0,ma=0;
    cin >> n;
    int ar[n];
    for (int i=0;i<n;i++){
        cin >> ar[i];
        ma += ar[i];
        if (res < ma){
            res = ma;
        }
        if (ma < 0){
            ma = 0;
        }
    }
    cout << res; 
    return 0;
}