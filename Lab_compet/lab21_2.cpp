#include <bits/stdc++.h>

using namespace std;

const int MAXN = 50;
const int MAXM = 500;
const int INF = 1e9;

int n, m;
int cap[MAXN+1][MAXN+1]; // capacity matrix
int flow[MAXN+1][MAXN+1]; // flow matrix
int parent[MAXN+1]; // parent array for BFS
bool visited[MAXN+1]; // visited array for BFS

// Find an augmenting path from s to t using BFS
bool bfs(int s, int t) {
    memset(visited, false, sizeof(visited));
    memset(parent, -1, sizeof(parent));
    queue<int> q;
    q.push(s);
    visited[s] = true;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v = 1; v <= n; v++) {
            if (!visited[v] && cap[u][v] - flow[u][v] > 0) {
                visited[v] = true;
                parent[v] = u;
                q.push(v);
            }
        }
    }
    return visited[t];
}

// Find the maximum flow from s to t using Edmonds-Karp algorithm
int maxFlow(int s, int t) {
    long totalFlow = 0;
    while (bfs(s, t)) {
        int pathFlow = INF;
        for (int v = t; v != s; v = parent[v]) {
            int u = parent[v];
            pathFlow = min(pathFlow, cap[u][v] - flow[u][v]);
        }
        for (int v = t; v != s; v = parent[v]) {
            int u = parent[v];
            flow[u][v] += pathFlow;
            flow[v][u] -= pathFlow;
        }
        totalFlow += pathFlow;
    }
    return totalFlow;
}

// Find the minimum cut between s and t
void minCut(int s, int t) {
    int minCost = maxFlow(s, t);
    vector<pair<int, int>> cutEdges;
    for (int u = 1; u <= n; u++) {
        if (visited[u]) {
            for (int v = 1; v <= n; v++) {
                if (!visited[v] && cap[u][v] > 0) {
                    cutEdges.push_back(make_pair(min(u, v), max(u, v)));
                }
            }
        }
    }
    // Sort and output the cut edges in ascending order of city number
    sort(cutEdges.begin(), cutEdges.end());
    for (auto edge : cutEdges) {
        cout << edge.first << " " << edge.second << endl;
    }
}

int main() {
    cin >> n >> m;
    memset(cap, 0, sizeof(cap));
    memset(flow, 0, sizeof(flow));
    for (int i = 0; i < m; i++) {
        int u, v, c;
        cin >> u >> v >> c;
        cap[u][v] += c;
        cap[v][u] += c;
    }
    minCut(1, 2);
    
    return 0;
}
