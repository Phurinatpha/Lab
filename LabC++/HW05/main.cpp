#include <iostream>
#include <stack>
#include <queue>
#include <string>
using namespace std;

bool isBalanced(string s) {
  string open_sym = "([{";
  string close_sym = ")]}";
  stack<char> st;

  for (int i = 0; i < s.length(); i++){
    if (close_sym.find(s[i]) != string::npos){
      if (!st.empty()){
        char top = st.top();
        if ((top == '(' && s[i] == ')') || (top == '[' && s[i] == ']') || (top == '{' && s[i] == '}')){
          st.pop();
        } else {
          return false;
        }
      } else {
        return false;
      } 
    } else if (open_sym.find(s[i]) != string::npos){
      st.push(s[i]);
    } else {
      return false;
    }
  }

  if (st.empty()){
    return true;
  }
  return false;
}

int main() {
  string s;
  cin >> s;
  while (s != "-1") {
    if(isBalanced(s)) {
      cout << "Parentheses are balanced" << endl;
    } else {
      cout << "Parentheses are not balanced" << endl;
    }
    cin >> s;
  }
    
}
