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
        int time = abs(b - a) / distance;
        if (abs(b - a) % distance != 0) {
            time += 1;
        }
        
        min_time = min(min_time, time);
        
    }

    if (min_time == numeric_limits<int>::max()) {
        cout << "-1" << endl;
    } else {
        cout << min_time << endl;
    }

    return 0;
}
