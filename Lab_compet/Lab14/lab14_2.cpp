#include <bits/stdc++.h>
using namespace std;

int knapSack(int W, int wt[], int val[], int n){
    int i, w;
    int K[n+1][W+1];
    for (i = 0; i <= n; i++){
        for (w = 0; w <= W; w++){
            if (i==0 || w==0)
                K[i][w] = 0;
            else if (wt[i-1] <= w)
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w]);
            else
                K[i][w] = K[i-1][w];
        }
    }
    return K[n][W];
}


int main(){
    int a;
    cin >> a;
    int val[a];
    int wt[a];
    for (int i=0;i<a;i++){
        cin >> val[i] >>wt[i];
    }

    int b,W,sum=0;
    
    cin >> b;
    int n = sizeof(val)/sizeof(val[0]);
    for (int i=0;i<b;i++){
        cin >> W;
        sum += knapSack(W, wt, val, n);
        
        // printf("check %d = %d\n", W,knapSack(W, wt, val, n));
    }
    
    cout << sum;
    return 0;
}

