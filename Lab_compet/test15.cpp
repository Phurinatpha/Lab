#include <iostream>
#include <vector>
#include <stack>

using namespace std;

const int MAX_SIZE = 20;

int dx[] = {0, 0, 1, -1}; // possible moves in x-axis
int dy[] = {1, -1, 0, 0}; // possible moves in y-axis

int n, m; // size of the map
int map[MAX_SIZE][MAX_SIZE]; // the map itself

bool visited[MAX_SIZE][MAX_SIZE]; // to mark visited rooms
int count_paths = 0; // to count the number of possible paths

void dfs(int x, int y) {
    visited[x][y] = true;

    if (map[x][y] == 2) { // found the treasure room
        count_paths++;
        visited[x][y] = false; // mark the room as unvisited
        return;
    }

    for (int i = 0; i < 4; i++) { // try all possible moves
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx >= 0 && nx < n && ny >= 0 && ny < m && map[nx][ny] != -1 && !visited[nx][ny]) {
            dfs(nx, ny); // recursively search the next room
        }
    }

    visited[x][y] = false; // mark the room as unvisited
}

int main() {
    cin >> n >> m;

    int start_x, start_y;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> map[i][j];

            if (map[i][j] == 1) { // found the entrance
                start_x = i;
                start_y = j;
            }
        }
    }

    dfs(start_x, start_y);

    cout << count_paths << endl;

    return 0;
}
