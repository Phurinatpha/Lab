#include <iostream>
#include "HW01.cpp"
using namespace std;

int main()
{
  CardList L;
  L.insert_back("Pokemon");
  L.insert_back("Natu");
  L.insert_back("Steelix");
  L.insert_back("Dragonite");
  L.insert_back("Mewmew");
  L.insert_back("Jakka");
  L.pop_back();
  L.pop_back();


  Card * curr = L.head;
  while(curr!=NULL) {
    cout << curr->name << endl;
    curr = curr->next;
  }
  return 0;
}
