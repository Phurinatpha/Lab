#include <bits/stdc++.h>
using namespace std;

int cutRod(int price[], int n){
   int val[n+1];
   val[0] = 0;
 
   for (int i = 1; i<=n; i++){
       int max_val = 0;
       for (int j = 0; j < i; j++)
            max_val = max(max_val, price[j] + val[i-j-1]);
       val[i] = max_val;
   }
 
   return val[n];
}

int main(){
    int size,wa;
    cin >> size;
    int arr[size];
    
    for (int i =0; i<size;i++){
        cin >> arr[i];
    }

    cin >> wa;
    cout << cutRod(arr, wa);
    
    return 0;
}
