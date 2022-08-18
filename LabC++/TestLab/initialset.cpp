#include<iostream>
#include<set>
using namespace std;
int main(){
// Empty Set - Increasing Order (Default) s1 = {}
set<int> s1;
// Empty Set - Decreasing Order s2 = {}
set<int, greater<int>> s2;
// Set with values
set<int, greater<int>> s3 = {6, 10, 5, 1}; // s3 = {10, 6, 5, 1}
// Initialize Set using other set
set<int, greater<int>> s4(s3); // s4 = {10, 6, 5, 1}
// Initializing a set from array
int arr[] = {10, 4, 5, 61};
set<int> s5(arr, arr+4); // s5 = {4, 5, 10, 61}
return 1;
}