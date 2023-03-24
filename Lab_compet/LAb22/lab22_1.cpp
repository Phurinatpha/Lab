#include<bits/stdc++.h> 
using namespace std; 
int main(){
  int n;cin>>n;
  // create an array to store number of ways to tile a grid of size 2xi
  int tile[n+1];
  // base case
  tile[0] = 0; tile[1] = 1;
  for(int i=2;i<=n;i++)
    tile[i]  = tile[i-1] + tile[i-2]; // use recursive formula
  cout<<tile[n];
}