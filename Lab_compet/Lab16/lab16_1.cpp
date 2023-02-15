#include <bits/stdc++.h>
using namespace std;


typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
int V, E, a, b, s;
vector<vii> AdjList;
vi p; // addition: the predecessor/parent vector
int main() {
    scanf("%d %d", &V, &E);
    AdjList.assign(V, vii());
    // assign blank vectors of pair<int, int>s to AdjList
    for (int i = 0; i < E; i++) {
        scanf("%d %d", &a, &b);
        AdjList[a].push_back(ii(b, 0));
        AdjList[b].push_back(ii(a, 0));
    }
    // we start from this source
    s = 5;
    
    vi dist(V, 1000000000); dist[s] = 0; // distance to source is 0
    queue<int> q; q.push(s); // start from source
    p.assign(V, -1); // to store parent information
    int layer = -1; // for our output printing purpose
    while (!q.empty()) {
        int u = q.front(); q.pop(); // queue: layer by layer!
        if (dist[u] != layer) printf("\nLayer %d: ", dist[u]);
        layer = dist[u];
        printf("visit %d, ", u);
        for (int j = 0; j < (int)AdjList[u].size(); j++) {
            ii v = AdjList[u][j]; // for each neighbors of u
            if (dist[v.first] == 1000000000) {
                dist[v.first] = dist[u] + 1; // v unvisited + reachable
                p[v.first] = u; //addition: the parent of vertex v->first is u
                q.push(v.first); // enqueue v for next step
        }
        }
    }
    return 0;
}