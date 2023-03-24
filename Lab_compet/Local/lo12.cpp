#include <iostream>
#include <vector>
#include <cmath>
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
    pair<int, int> start = rocks[0];
    pair<int, int> end = rocks[1];
    double min_distance = sqrt(pow(end.first - start.first, 2) + pow(end.second - start.second, 2));
    for (int i = 2; i < n; i++) {
        double distance = sqrt(pow(rocks[i].first - start.first, 2) + pow(rocks[i].second - start.second, 2));
        if (distance < min_distance) {
            min_distance = distance;
        }
    }
    printf("%.3f\n", min_distance);
    return 0;
}
