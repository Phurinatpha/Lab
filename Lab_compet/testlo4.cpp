#include <bits/stdc++.h>
using namespace std;
 
int maxSubArraySum(int a[], int size)
{
    int max_so_far = INT_MIN, max_ending_here = 0;
 
    for (int i = 0; i < size; i++) {
        max_ending_here = max_ending_here + a[i];
        if (max_so_far < max_ending_here)
            max_so_far = max_ending_here;
 
        if (max_ending_here < 0)
            max_ending_here = abs(max_ending_here);
    }
    return max_so_far;
}
 
int main()
{
    const int MAX_SIZE = 1000;
    int a[MAX_SIZE];
    int n;
    // for (int j =0 ;j<5;j++){
    //     cin >> n;
    //     for (int i = 0 ;i<n;i++){
    //         cin >> a[i];
    //     }
    //     int max_sum = maxSubArraySum(a, n);
    //     cout << max_sum << endl;
    // }
    cin >> n;
    for (int i = 0 ;i<n;i++){
        cin >> a[i];
    }
    int max_sum = maxSubArraySum(a, n);
    cout << max_sum << endl;
    return 0;
}
