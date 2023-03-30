#include <bits/stdc++.h>
using namespace std;

int dr[] = {1,1,0,-1,-1,-1, 0, 1};
int dc[] = {0,1,1, 1, 0,-1,-1,-1};
char grid[99][99];

int floodfill(int r, int c, char c1, char c2, int rows, int cols) {
    if (r < 0 || r >= rows || c < 0 || c >= cols) return 0;
    if (grid[r][c] != c1) return 0;

    int ans = 1; 
    grid[r][c] = c2;
    for (int d = 0; d < 8; d++)
        ans += floodfill(r + dr[d], c + dc[d], c1, c2, rows, cols);
    return ans;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string input,s;
    int rows = 0, cols = 0;

    // Taking the input
    while (getline(cin, input)) {
        if (isdigit(input[0])) {
            stringstream ss(input);
            ss >> rows >> cols;
            break;
        }
        for (int i = 0; i < cols; i++)
            grid[rows][i] = input[i];
        rows++;
    }

    // Processing the queries
    int r, c;
    while (cin >> r >> c) {
        char c1 = 'W';
        cin >> s;
        int ans = floodfill(r, c, c1, s[0], rows, cols);
        cout << ans << endl;
    }

    return 0;
}
