#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,ma=0; 
    cin >> n;
    int arr2[n-1];
    int arr[n];
    
    for (int i=0;i<n;i++){
        cin >> arr[i];
    }

    for (int i = 0; i < n-1 ; i++){
        arr2[i] = arr[i] * arr[i+1];
        ma = max(ma,arr2[i]);
    }
    
    
    if (ma > 0)
        cout << ma << endl;
    else
        cout << 0 << endl; 
    
 
    return 0;
}

