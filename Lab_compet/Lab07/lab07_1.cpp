#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,m,a,be,end; 
    cin >> n >> m;
    int prefixSum[n];
    int arr[n];
    
    for (int i=0;i<n;i++){
        cin >> a;
        arr[i] = a;
    }

    prefixSum[0] = arr[0];
    for (int i = 1; i < n; i++)
        prefixSum[i] = prefixSum[i - 1] + arr[i];
    
    for (int k=0;k<m;k++){
        cin >> be >> end;
        cout << prefixSum[end] - prefixSum[0,be-1] << "\n";
    }


    return 0;
}

