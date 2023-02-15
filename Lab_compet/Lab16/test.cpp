#include <bits/stdc++.h>
using namespace std;
const int N = 100010;
vector<int> dfs_num;
vector<int> adj[N];
void dfs(int s){
    printf("%d\n", s);
    dfs_num[s] = true;
    for (auto u : adj[s]) {
        if(dfs_num[u]==-1)
        dfs(u);
      }
}

int main(){
    int n, m; // nodes, edges
    scanf("%d%d", &n, &m);
    dfs_num.assign(n, -1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        scanf("%d%d", &u, &v);
        adj[u].push_back(v);
        adj[v].push_back(u);
      }
    int s; // start
    scanf("%d", &s);
    dfs(s);
    return 0;
}