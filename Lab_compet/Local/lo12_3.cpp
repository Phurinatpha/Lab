#include <iostream>
#include <vector>
#include <cmath>
#include <limits>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<int, int>> rocks;
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        rocks.push_back(make_pair(x, y));
    }

    double min_distance = numeric_limits<double>::max();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            double distance = sqrt(pow(rocks[j].first - rocks[i].first, 2) + pow(rocks[j].second - rocks[i].second, 2));
            if (distance < min_distance) {
                min_distance = distance;
            }
        }
    }
    printf("%.3f\n", min_distance);
    return 0;
}
