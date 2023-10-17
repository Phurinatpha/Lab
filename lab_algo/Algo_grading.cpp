#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int findLongestSubsequence(vector<int> &correctOrder, vector<int> &answers) {
    int n = correctOrder.size();
    vector<int> dp(n + 1, 0);

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (correctOrder[i - 1] == answers[j - 1]) {
                dp[j] = *max_element(dp.begin(), dp.begin() + j) + 1;
            }
        }
    }

    return *max_element(dp.begin(), dp.end());
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;
    vector<int> correctOrder(N);
    for (int i = 0; i < N; i++) {
        cin >> correctOrder[i];
    }

    for (int i = 0; i < M; i++) {
        vector<int> answers(N);
        for (int j = 0; j < N; j++) {
            cin >> answers[j];
        }
        cout << findLongestSubsequence(correctOrder, answers) << '\n';
    }

    return 0;
}
