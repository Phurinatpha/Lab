#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,m,a,b,be,end; 
    cin >> n >> m;
    int prefixSum[n];
    vector<int> arh;
    vector<int> arl;
    
    for (int i=0;i<n;i++){
        cin >> a;
        arh.push_back(a);
    }

    for (int i=0;i<n;i++){
        cin >> b;
        arl.push_back(b);
    }

    prefixSum[0] = arl[0];
    for (int i = 1; i < n; i++)
        prefixSum[i] = prefixSum[i - 1] + arl[i];
    
    for (int k=0;k<m;k++){
        cin >> be >> end;

        auto max_it = max_element(arh.begin()+be, arh.begin()+end+1);
    
        cout << *max_it << " "<< prefixSum[end] - prefixSum[0,be-1] << "\n";
    }


    return 0;
}

