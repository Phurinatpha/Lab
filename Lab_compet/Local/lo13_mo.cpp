#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c, n;
    cin >> a >> b >> c >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int min_time = INT_MAX;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int dist = abs(b - a);
            int time = 0;
            int warp_dist = arr[i];
            int warp_count = 0;
            while (dist > 0) {
                if (dist <= warp_dist) {
                    time++;
                    break;
                }
                if (warp_count > 0) {
                    dist -= warp_dist;
                    warp_count--;
                } else {
                    warp_count = arr[j] - 1;
                    warp_dist += c;
                }
                time++;
            }
            if (dist == 0) {
                min_time = min(min_time, time);
            }
        }
    }
    if (min_time == INT_MAX) {
        cout << -1 << endl;
    } else {
        cout << min_time << endl;
    }
    return 0;
}
