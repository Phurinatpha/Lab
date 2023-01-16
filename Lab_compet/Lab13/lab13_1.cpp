#include <bits/stdc++.h>
using namespace std;

int CHANGE(int n){
    int C[n+1], min,k;
    cin >> k;
    int d[k];
    for (int i =0; i<k;i++){
        cin >> d[i];
    }
    C[0] = 0; //base case
    for(int p = 1; p <= n; p++){
        min = n;
        for (int i = 0; i < k; i++){//ลองทุกเหรียญ
            if (p >= d[i]){//ถ้าค่าของเหรียญมากกว่าไม่ท า
                if(C[p - d[i]] + 1 < min){
                    min = C[p - d[i]] + 1;
                }
            }
        }
        C[p] = min;
    }
    return C[n];
}


int main(){
    int wa;
    cin >> wa;
    cout << CHANGE(wa);
    
    return 0;
}