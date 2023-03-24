#include <bits/stdc++.h>

using namespace std;

const int MAX = 100;
int n, m, c = 0, no_entry = 0;
int matrix[MAX][MAX];
bool visited[MAX][MAX];

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

int dfs(int x, int y, int cnt)
{
    visited[x][y] = true;
    int longest_path = 0;
    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && matrix[nx][ny] != -1)
        {
            if (matrix[nx][ny] == 2)
            {
                // cout << "cnt : " << cnt << endl;
                if(cnt == (m*n)-no_entry-2 ){
                    c++;
                }
                longest_path = max(longest_path, cnt + 1);
            }
            else
            {
                longest_path = max(longest_path, dfs(nx, ny, cnt + 1));
            }
        }
    }
    visited[x][y] = false;
    return longest_path;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;

    int start_x, start_y;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> matrix[i][j];
            if (matrix[i][j] == -1){
                no_entry++;
            }
            if (matrix[i][j] == 1)
            {
                start_x = i;
                start_y = j;
            }
        }
    }

    dfs(start_x, start_y, 0);
    // cout << longest_path << endl;
    cout << c << endl;
    return 0;
}