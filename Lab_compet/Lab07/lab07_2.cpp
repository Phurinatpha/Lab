#include <bits/stdc++.h>
using namespace std;
int query(int r, int l, int n, long max_block[], long arr[]){
    long m = arr[l];
    int blk_sz = ceil(sqrt(n));
    while (l < r && l % blk_sz != 0 && l != 0){
        // traversing first block in range
        if (arr[l] > m)
        {
            m = arr[l];
        }
        l++;
    }
    while (l + blk_sz <= r){
        // traversing completely overlapped blocks in range
        if (max_block[l / blk_sz] > m)
        {
            m = max_block[l / blk_sz];
        }
        l += blk_sz;
    }
    while (l <= r){
        // traversing last block in range
        if (arr[l] > m){
            m = arr[l];
        }
        l++;
    }
    return m;
}

void Build(long input[], int n, long arr[], long max_block[]){
    int blk_idx = -1;
    int blk_sz  = ceil(sqrt(n));
    for (int i = 0; i < n; i++){
        arr[i] = input[i];
        if (i % blk_sz  == 0){
            blk_idx++;
            max_block[blk_idx] = arr[i];
        }

        max_block[blk_idx] = max(max_block[blk_idx], arr[i]);
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    long n = 0, m = 0, num = 0, end = 0, be = 0, blk_sz = 0, highest = 0;
    cin >> n >> m;
    blk_sz = ceil(sqrt(n));
    long arl[n], arh[n], high[m], max_block[n], sum_block[n], arr[n];
    int prefixSum[n];

    for (int i = 0; i < n; i++) {
        cin >> num;
        arh[i] = num;
    }
    
    Build(arh, n, arr, max_block); 
    num = 0;
    for (int i = 0; i < n; i++){
        cin >> num;
        arl[i] = num;
    }

    prefixSum[0] = arl[0];
    for (int i = 1; i < n; i++)
        prefixSum[i] = prefixSum[i - 1] + arl[i];
    
    for (int k=0;k<m;k++){
        cin >> be >> end;
        high[k] = query(end, be, n, max_block, arh);
        cout << high[k] << " "<< prefixSum[end] - prefixSum[0,be-1] << "\n";
    }


    return 0;
}

