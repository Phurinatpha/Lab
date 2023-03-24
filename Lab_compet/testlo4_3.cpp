#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int solve(vector<int>& boxes, int left, int right) {
    if (left == right) {
        return boxes[left];
    }
    int chooseLeft = boxes[left] - solve(boxes, left + 1, right);
    int chooseRight = boxes[right] - solve(boxes, left, right - 1);
    return max(chooseLeft, chooseRight);
}

int main() {
    int n;
    cin >> n;

    vector<int> boxes(n);
    for (int i = 0; i < n; i++) {
        cin >> boxes[i];
    }

    int scoreDiff = solve(boxes, 0, n-1);
    cout << scoreDiff << endl;

    return 0;
}
