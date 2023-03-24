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
            max_ending_here = 0;
    }
    return max_so_far;
}

int main()
{
    const int MAX_SIZE = 1000;
    int a[MAX_SIZE];
    int n;
    for (int j =0 ;j<5;j++){
        cin >> n;
        for (int i = 0 ;i<n;i++){
            cin >> a[i];
        }
        int sum1 = 0, sum2 = 0, max_diff = INT_MIN;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                sum1 += a[i];
            } else {
                sum2 += a[i];
            }
            if (i > 0 && i < n - 1) {
                max_diff = max(max_diff, abs(sum1 - sum2));
            }
        }
        int ans = maxSubArraySum(a, n);
        ans = max(ans - max_diff, max_diff - ans);
        cout << ans << endl;
    }
    return 0;
}
