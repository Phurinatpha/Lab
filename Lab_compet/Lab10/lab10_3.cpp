#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    long n,a;
    long co = 0,co2 = 0;
    cin >> n;
    long s[n];
    for (long i=0;i<n;i++){
        cin >> a;
        s[i] = a;
    } 

    for (long b = 0; b < (1<<n); b++) {
        vector<long> subset;
        vector<long> sub;
        for (long i = 0; i < n; i++) {
            if (b&(1<<i)) {
                subset.push_back(i);
            }
        }
        
        co = 0;
        for(auto &l:subset){
            if (co < 6)
                sub.push_back(s[l]);
            co++;
        }

        if (sub.size() == 6 and co2 < n){
            for (auto x:sub){
                
                cout << x << " ";
                
            }
            co2 ++;
            cout<<endl;
        }
    
    }
    

    return 0;
}
