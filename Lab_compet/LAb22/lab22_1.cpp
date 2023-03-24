#include<bits/stdc++.h> 
using namespace std; 
int main(){
  int n;cin>>n;

  vector<int> f(n + 1);
  f[0] = 1;
  f[1] = 1;
  f[2] = 1;
  for(int i = 3; i <= n; i++)
  {
      f[i] = f[i-1] + f[i-3];
  }
  cout<<f[n];
}

int num_ways(int n, int m) {
  int T[n+1];
  memset(T, 0, sizeof(T));
  T[0] = 1;
  for (int i = 1; i <= n; i++) {
    T[i] = T[i-1];
    if (i >= m) {
      T[i] += T[i-m];
    }
  }
  return T[n];
}