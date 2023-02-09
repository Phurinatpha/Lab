#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long n; 
    cin >> n;
    
    for (long long i=0;i<n;i++){
        if (n%(i+1) == 0)
            cout << i << " ";
    }
    
    return 0;
}

