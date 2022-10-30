#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Village{
     int numHouse;
     vector<int> *adjLists;
     bool *bfs_visited;
     bool *dfs_visited;

    
public:
     Village(int V){
          numHouse = V;
          adjLists = new vector<int>[V];

     }
     void addRoad(int src, int dest){
          adjLists[src].push_back(dest);
          adjLists[dest].push_back(src);
     }

     void BFS(int firstHouse){
          bfs_visited = new bool[numHouse];
          for (int i = 0; i < numHouse; i++)
               bfs_visited[i] = false;
          queue<int> q;
          q.push(firstHouse);
          while(!q.empty()){
               int u = q.front();
               q.pop();
               if(bfs_visited[u])
                    continue;
               bfs_visited[u] = true;
               cout<<u<<" ";
               sort_adjLists();
               vector<int>::iterator it;
               for(it = adjLists[u].begin(); it!=adjLists[u].end(); it++){
                    if(!bfs_visited[*it])
                         q.push(*it);
               }
          }
     }

     void DFS(int firstHouse){
          dfs_visited = new bool[numHouse];
          for (int i = 0; i < numHouse; i++)
               dfs_visited[i] = false;
          DFSVISIT(firstHouse);
          for(int i=0;i<numHouse;i++){
               if(dfs_visited[i]==false)
                    DFSVISIT(i);
          }
     }

     void DFSVISIT(int vertex){
          dfs_visited[vertex] = true;
          cout<< vertex<< " ";
          sort_adjLists();
          vector<int>::iterator it;
          for(it = adjLists[vertex].begin(); it!=adjLists[vertex].end(); it++){
               if(!dfs_visited[*it])
                    DFSVISIT(*it);
          }
     }

     void sort_adjLists(){
          for (int i = 0; i < numHouse; i++){
               sort(adjLists[i].begin(), adjLists[i].end());
          }
    }
    
};




