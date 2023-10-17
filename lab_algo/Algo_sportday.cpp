#include <bits/stdc++.h>
using namespace std;

struct Interval {
    int beginn, endd;
    bool operator<(const Interval& a) const {
        return endd < a.endd || (endd == a.endd && beginn < a.beginn);
    }
};

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<Interval> intervals;
        for (int i = 0; i < n; i++) {
            int beginn, endd;
            cin >> beginn >> endd;
            intervals.emplace_back(Interval{beginn, endd});
        }

        sort(intervals.begin(), intervals.end());

        queue<Interval> opt;
        int count = 0;
        int finish = -1;  // To handle intervals that beginn at 0
        for (const Interval& interval : intervals) {
            if (interval.beginn >= finish) {
                opt.push(interval);
                finish = interval.endd;
                count++;
            }
        }

        cout << count << endl;
    }

    return 0;
}
