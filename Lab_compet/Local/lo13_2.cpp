#include<bits/stdc++.h> 

using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    vector<int> distances(c);
    for (int i = 0; i < c; i++) {
        cin >> distances[i];
    }

    int min_time = numeric_limits<int>::max();
    for (int distance : distances) {
        if (abs(b - a) % distance == 0) {
            int time = abs(b - a) / distance;
            min_time = min(min_time, time);
        }
        else {
            int time1 = abs(b - a) / distance;
            int time2 = time1 + 1;
            int remainder = abs(b - a) % distance;
            if (remainder <= distance / 2) {
                min_time = min(min_time, time1);
            }
            else {
                min_time = min(min_time, time2);
            }
        }
    }

    if (min_time == numeric_limits<int>::max()) {
        cout << "-1" << endl;
    } else {
        cout << min_time << endl;
    }

    return 0;
}
