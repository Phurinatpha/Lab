#include <bits/stdc++.h>
using namespace std;
 
class Graph {
    int V;
    list<int>* adj;
 
    void DFSUtil(int v, bool visited[]);
 
    public:
        Graph(int V);
        void addEdge(int v, int w);
        int NumberOfconnectedComponents();
};
 

int Graph::NumberOfconnectedComponents(){
 
    bool* visited = new bool[V];
 
    int count = 0;
    for (int v = 0; v < V; v++)
        visited[v] = false;
 
    for (int v = 0; v < V; v++) {
        if (visited[v] == false) {
            DFSUtil(v, visited);
            count += 1;
        }
    }
 
    return count;
}
 
void Graph::DFSUtil(int v, bool visited[]){
 
    visited[v] = true;
    list<int>::iterator i;
 
    for (i = adj[v].begin(); i != adj[v].end(); ++i)
        if (!visited[*i])
            DFSUtil(*i, visited);
}
 
Graph::Graph(int V){
    this->V = V;
    adj = new list<int>[V];
}
 
void Graph::addEdge(int v, int w){
    adj[v].push_back(w);
    adj[w].push_back(v);
}
 
int main(){
    char maxch, a, b;

    cin >> maxch;

    Graph g((static_cast<int>(maxch) - 65) + 1);

    while(cin >> a >> b) {
        g.addEdge(static_cast<int>(a) - 65, static_cast<int>(b) - 65);
    }

    cout << g.NumberOfconnectedComponents();
 
    return 0;
}